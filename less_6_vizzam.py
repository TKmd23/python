# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help your {self.work}. After i'll do my {work}"
#
#
# helper = Helper("homework")
# print(helper("cleaning"))
# --------------------------------------

def helper(work):
    work_in_memory = work

    def h(work_new):
        return f"I will help yo with {work_in_memory}. After I'll do my {work_new}"
    return h


hi = helper("homework")
print(hi("clean"))
print(hi("drive"))

