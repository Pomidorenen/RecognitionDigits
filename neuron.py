def recognize_digit(array: list[int], templates: dict[int, list[int]]) -> dict[int, float]:
    scores = {}

    for digit, template in templates.items():
        matched_active = 0
        total_active = 0
        extra_pixels = 0
        critical_misses = 0

        for i in range(len(array)):
            if template[i] == 1:
                total_active += 1
                if array[i] == 1:
                    matched_active += 1
                else:
                    critical_misses += 1
            elif array[i] == 1:
                extra_pixels += 1

        if total_active == 0:
            scores[digit] = 0.0
        else:
            score = (matched_active / total_active) * 0.7
            score -= (extra_pixels / len(array)) * 0.3
            score -= (critical_misses / total_active) * 0.2  #

            scores[digit] = max(0.0, score)
    return scores