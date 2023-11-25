# original = [['dogs', 'puppies'], ['cats', "kittens"]]
# copied_version = original[:]สร้างlist ที่มีขนาดเท่ากับ original ขนาด2เท่านั้น
# print(copied_version)
# print(copied_version is original)ไม่ใชoriginal
# print(copied_version == original)ข้างในเหมือนกัน
# original[0].append(["canines"]) copiedเปลี่ยนเพราะว่า เมื่อเพิ่มแล้วขนาดcopied เท่าเดิม
# print(original)
# print("-------- Now look at the copied version -----------")
# print(copied_version)
# import copy
# original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
# shallow_copy_version = original[:]
# deeply_copied_version = copy.deepcopy(original)สร้างจากoriginal ณ ตอนนั้น
# original.append("Hi there") shallowไม่เปลี่ยนเพราะว่า shallowต้องมีขนาดเท่าเดิมเสมอ
# original[0].append(["marsupials"])shallowเปลี่ยนเพราะว่า เปลี่ยนแล้วshallowมีขนาดเท่าเดิม
# print("-------- Original -----------")
# print(original)
# print("-------- deep copy -----------")
# print(deeply_copied_version)
# print("-------- shallow copy -----------")
# print(shallow_copy_version)
