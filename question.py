conversion = ["Hello nerd, what can I do for you?",
              "Hello there, what's good?",
              "What now?",
              "this better be good, you disrupted my beauty sleep"]

daygreet = [
    "good morning",
    "good afternoon",
    "good evening",
    "good night",
]

allowed = [
    "kid", "friend", "pal", "buddy", "hallo", "Jack"
]

remarks = {"are you sure":"Am certain",
           "how sure are you":"Very sure",
           "am fine":"Awesome",
           "thanks":"you are welcome.",
           "thank you":"don't mention it",
           "what is your gender": "what do you think",
           "are you a girl or a boy": "what do you think",
           "I am fine":"that's great, what's good",
           "am alright":"fantastic, what's up",
           "not good":"what's wrong, actually i don't care",
           "what's up": "don't ask me, you're the one with eyes",
           "really":"yes, really"}

def get_last_item(some):
    words = some.split()
    return words[-1]
