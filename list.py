def demo_basic_operation():
    flowers = ["calla", "lily", "jasmine"]
    print(flowers)
    flowers = flowers + ["forget me not", "sunflower", "ivy", "gypso"]
    print(flowers)
    del flowers[1]
    print(flowers)
    flowers.remove("jasmine")
    print(flowers)
    sorted_flowers = sorted(flowers)
    print(sorted_flowers)
    print(flowers)
    flowers.sort()
    print(flowers)
    flowers.append("carnation")
    print(flowers)


def demo():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    # slice
    print(flowers[1:4])  # [inclusive:exclusive]
    print(flowers[-1])
    print(flowers[-1:-4:-1])
    print(flowers[:3])
    print(flowers[2:])


demo()
#list demo1
def loop_list():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    # for f in flowers:
    #     print(f)
    #
    # for i in range(len(flowers)):
    #     print("{}. {}".format(i+1, flowers[i]))

    for i, e in enumerate(flowers):
        print("{}. {}".format(i+1, e))

def loop_list2():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "Japan", "ญี่ปุ่น"),
        ("kr", "Korea", "เกาหลีใต้")
    ]
    # for country in countries:
    #     # print(country)
    #     print(country[2])

    # iterate, traverse, loop
    for i, country in enumerate(countries):
        # print(country)
        print("{}. {}".format(i + 1, country[2]))

# loop_list()
loop_list2()
#list demo2
