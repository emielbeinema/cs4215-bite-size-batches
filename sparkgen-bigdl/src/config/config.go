package config

import (
  "encoding/json"
  "log"
  "io/ioutil"
  "os"
  "strconv"
)

type Configuration struct {
  json map[string]interface{}
}

var instance *Configuration = nil

var Configfile string

func load() *Configuration {
  if instance == nil {
    instance = &Configuration{}
  }
  
  if Configfile == "" {
    Configfile = "conf.json"
  }
  
  file, err := os.Open(Configfile)
  if err != nil {
    log.Printf("Loading configuration failed %s\n", err.Error())
    return instance
  }

  bytes, err := ioutil.ReadAll(file)
  if err != nil {
    log.Printf("Reading configuration failed %s\n", err.Error())
    return instance
  }

  var f interface{}
  err = json.Unmarshal(bytes, &f)
  if err != nil {
    log.Printf("Parsing configuration failed %s\n", err.Error())
    return instance
  }

  instance.json = f.(map[string]interface{})
  
  log.Printf("Current configuration from %s:\n%s\n", Configfile, string(bytes))
  
  return instance
}

func GetInt64(key, defaultVal string) int64 {
  val := Get(key, defaultVal)
  ret, err := strconv.ParseInt(val, 10, 64)
  if err != nil {
    log.Printf("Parsing integer(%s) failed %s\n", val, err.Error())
  }
  return ret
}

func GetFloat64(key, defaultVal string) float64 {
  val := Get(key, defaultVal)
  ret, err := strconv.ParseFloat(val, 64)
  if err != nil {
    log.Printf("Parsing float(%s) failed %s\n", val, err.Error())
  }
  return ret
}

func Get(key, defaultVal string) string {
  if instance == nil {
    instance = load()
  }
  if instance.json == nil {
    return defaultVal
  }
  val, exists := instance.json[key]
  if exists {
    switch v := val.(type) {
    case string:
      return v
    default:
      return defaultVal
    }
  }
  return defaultVal
}

func GetArray(key string, defaultVal []string) []string {
  if instance == nil {
    instance = load()
  }
  if instance.json == nil {
    return defaultVal
  }
  val, exists := instance.json[key]
  if exists {
    tmpSlice := val.([]interface {})
    finalSlice := make([]string, 0, len(tmpSlice))
    for _, i := range tmpSlice {
      finalSlice = append(finalSlice, i.(string))
    }
    return finalSlice
  }
  return defaultVal
}
