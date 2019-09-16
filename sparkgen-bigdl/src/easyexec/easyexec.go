package easyexec

import (
        "os/exec"
        "strings"
)

func Cmd(cmd string) *exec.Cmd {
        var args []string
        tokens := strings.Fields(cmd)
        for i, token := range tokens {
                if i != 0 {
                        args = append(args, token)
                }
        }
        return exec.Command(tokens[0], args...)
}