#!/usr/bin/env python3
from sys import argv
from collections import Counter
"""
Curry selector application
Python 3
Windows
"""


# OOP
class CurryHandler():
    """
    Curry Handler: Given an input with N types of curry
    and X Customers with N <= curry filling types, produces
    an optimal daily menu of curries.
    """

    def __init__(self, orders):
        self.orders = [x.split() for x in orders]
        self.total_curries = int(self.orders.pop(0)[0])
        self.customer_selections = []
        self.custos = []
        self.menu = ["V"] * self.total_curries
        self.poplist = set()
        self.locked = [False] * self.total_curries
        self.nm = False

    def select_curry(self):
        """
        Effectively a method wrapper to run class methods in series after
        initialization; Eventually returns our output.
        """
        self.handle_selection()
        self.first_pass()
        if self.nm:
            return "No solution exists"
        self.second_pass()
        if self.nm:
            return "No solution exists"
        self.final_check()
        if self.nm:
            return "No solution exists"
        else:
            todays_menu = "".join(self.menu)
        return todays_menu

    def handle_selection(self):
        """
        Codify customer preferences - 1 V 3 M 5 V = [V, 0, M, 0, V]
        """
        for customer in self.orders:
            choices = ["/"] * self.total_curries
            for k in range(len(customer)):
                if k % 2 == 0:
                    position = (int(customer[k]) - 1)  # -1?
                    if customer[k + 1].isalpha():
                        choices[position] = customer[k + 1]
            self.customer_selections.append(choices)

    def first_pass(self):
        """
        Find single preference customers, lock the menu index of their
        selection, and remove them from 'custos'.
        """
        self.custos = self.customer_selections
        for customer in self.custos:
            tally = Counter(customer)
            if tally["/"] == (self.total_curries - 1) and (tally["M"] == 1 or
                                                           tally["V"] == 1):
                if tally["M"] == 1:
                    indo = customer.index("M")
                    if self.menu[indo] == "V" and self.locked[indo]:
                        self.nm = True
                        break
                    else:
                        self.menu[indo] = "M"
                        self.locked[indo] = True
                        self.custos.remove(customer)
                else:
                    indo = customer.index("V")
                    if self.menu[indo] == "M" and self.locked[indo]:
                        self.nm = True
                        break
                    else:
                        self.menu[indo] = "V"
                        self.locked[indo] = True
                        self.custos.remove(customer)

    def second_pass(self):
        """
        Identify if only 1 remaining cust. in custos.
        Ignore null preferences.
        Check customer prefs against current menu.
        If match and locked, remove cust.
        If match and not locked, lock and remove cust.
        If no match and index locked, nullify customer preference : "/".
        If not matched and not locked and last cust., flip menu index value,
        lock, and remove cust.
        """
        for cust in self.custos:
            last = len(self.custos) == 1
            for i in range(len(cust)):
                if cust[i] == "/":
                    continue
                if self.compare_items(cust[i], self.menu[i]) == "Match":
                    if self.locked[i]:
                        if cust in self.custos:
                            self.custos.remove(cust)
                        else:
                            continue
                    else:
                        if last:
                            self.locked[i] = True
                            if cust in self.custos:
                                self.custos.remove(cust)
                if self.compare_items(cust[i], self.menu[i]) == "NoMatch":
                    if self.locked[i]:
                        cust[i] = "/"
                    else:  # We count potential menu item switch
                        if last:
                            self.menu[i] = cust[i]
                            self.locked[i] = True
                            self.custos.remove(cust)

    def compare_items(self, cp, mi):
        """
        Compare customer preference to menu index, return string.
        """
        if cp == mi:
            result = "Match"
        else:
            result = "NoMatch"
        return result

    def final_check(self):
        """
        Check original codified cust. prefs against proposed menu. If at least
        one match in each customer, produce menu. Otherwise return 'No
        solution exists'.
        """
        results = []
        for cust in self.customer_selections:
            cust_matches = []
            for pref in cust:
                pindo = cust.index(pref)
                if pref == "/":
                    cust_matches.extend("/")
                else:
                    if self.compare_items(pref, self.menu[pindo]) == "Match":
                        cust_matches.extend("Y")
                    else:
                        cust_matches.extend("N")
            if "Y" in cust_matches:
                results.extend("Y")
            else:
                results.extend("N")
        if "N" in results:
            self.nm = True

# Procedural
with open(argv[1], "r") as f:
    orders = f.readlines()
f.close()
todays_curry = CurryHandler(orders)
print(todays_curry.select_curry())
