package day5

import "regexp"

func GatherRules(rules string) map[string][]string{
	rulesRegex := regexp.MustCompile(`((\d+)\|(\d+))`)
	result := make(map[string][]string)

	for _, value  := range rulesRegex.FindAllStringSubmatch(rules, -1) {
		result[value[3]] = append(result[value[3]], value[2])
	}

	return result
}