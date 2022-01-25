#!/usr/bin/env python3
import random


class CurryInputGenerator():
    """
    Creating test inputs, especially longer ones, is painful.
    This class generates a random number of curries (max 10),
    a random number of customers (max 20), number of cust curry
    prefs (max total curries), and creates input to match sample
    format. Another random check determines if the cust is non-
    vegetarian, and randomly switches on V pref to M. As this is
    difficult to visually trace, I added a test output that puts
    out codified customer preferences for easier manual tracing.
    """
    def __init__(self):
        self.inp = list()
        self.customers = list()
        self.total_cur = 0
        self.total_cust = 0
        self.test = list()

    def input_gener8r(self):
        self.total_cur = random.randint(1, 10)
        print("DEBUG - total curries: {}".format(self.total_cur))
        self.total_cust = random.randint(1, 20)
        print("DEBUG - total custos: {}".format(self.total_cust))
        self.inp.append("{}\n".format(str(self.total_cur)))
        print("DEBUG - len custos: {}".format(len(self.customers)))
        for i in range(self.total_cust):
            # how many curry prefs a cust has
            customer = []
            if self.total_cur == 1:
                total_cp = 1
            else:
                total_cp = random.randint(1, self.total_cur)
            # menu index preferences
            menu_items = []
            # bool to handle loop
            finished = False
            while not finished:
                # attempts = 0
                print("Entered Loop")
                if len(menu_items) == total_cp:
                    finished = True
                mi = random.randint(1, self.total_cur)
                if mi not in menu_items:
                    menu_items.append(mi)
                    # attempts += 1
            print("Exited Loop")
            menu_items.sort()
            for item in menu_items:
                customer.append(str(item))
                customer.append("V")
            carni = random.randint(0, 1)
            print("DEBUG - carnivore?: {}".format(carni))
            if carni == 1:
                complete = False
                while not complete:
                    switch = random.randint(0, (len(customer) - 1))
                    if customer[switch] == "V":
                        customer[switch] = "M"
                        complete = True
            final_pref = ""
            for item in customer:
                final_pref += "{} ".format(item)
            final_pref += "\n"
            print("DEBUG -cust string: {}".format(final_pref))
            self.inp.append(final_pref)
        inpver = random.randrange(1, 1000)
        test_filename = "../sample_inputs/test/test{}.txt".format(inpver)
        input_filename = "../sample_inputs/input{}.txt".format(inpver)
        print("DEBUG - check filename: {}".format(input_filename))
        f = open(input_filename, "w+")
        for i in range(len(self.inp)):
            f.writelines(str(self.inp[i]))
        f.close()
        self.generate_test(test_filename)

    def generate_test(self, test_filename):
        print(self.inp)
        info = [x.split() for x in self.inp]
        info.pop(0)
        for customer in info:
            choices = ["/"] * self.total_cur
            for k in range(len(customer)):
                if k % 2 == 0:
                    position = (int(customer[k]) - 1)  # -1?
                    if customer[k + 1].isalpha():
                        choices[position] = customer[k + 1]
            self.test.append(choices)
        g = open(test_filename, "w+")
        for line in self.test:
            g.writelines("{}\n".format(line))
        g.close()

next = CurryInputGenerator()
next.input_gener8r()
