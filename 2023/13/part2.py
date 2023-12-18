from day13 import *

total_sum = 0

for i, pattern in enumerate(patterns):
    rowToIgnore = findRowReflection(pattern)
    colToIgnore = findColumnReflection(pattern)

    (smudgeHasBeenFixedRow, smudgePosRow) = findSmudgeThatCreatesNewRowReflection(pattern, rowToIgnore - 1)
    (smudgeHasBeenFixedCol, smudgePosCol) = findSmudgeThatCreatesNewColumnReflection(pattern, colToIgnore -1)

    if smudgeHasBeenFixedRow:
        smudgePos = smudgePosRow
    else:
        smudgePos = smudgePosCol

    patternFixed = pattern.copy()
    newString = patternFixed[smudgePos[0]]
    newString = newString[:smudgePos[1]] + ("#" if newString[smudgePos[1]] == "." else ".") + newString[smudgePos[1] + 1:]
    patternFixed[smudgePos[0]] = newString

    rowReflection = findRowReflection(patternFixed, rowToIgnore - 1)
    colReflection = findColumnReflection(patternFixed, colToIgnore - 1)

    if rowReflection != -1:
        total_sum += rowReflection * 100
    elif colReflection != -1:
        total_sum += colReflection

print(total_sum)
