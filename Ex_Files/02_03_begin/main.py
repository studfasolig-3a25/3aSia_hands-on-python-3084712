NAMES = ["Jef", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JEF = NAMES[0]
PAUL = NAMES[1]

JEF_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JEF_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
