"""
The Challenge

Baker Brie has a number of franchisees, each of which sells baked goods to 
consumers. 
Having reached the milestone of being in business for 13 years, Baker Brie 
will celebrate by awarding bonuses based on sales. 
The bonuses depend on sales per day and sales per franchisee. 
Here's how the bonuses work:
- For every day on which the total sales across all franchisees is a 
multiple of 13, that multiple will be given as bonuses. 
For example: 
a day where the franchisees sold a combined 26 baked goods will add 
26/ 13 = 2 bonuses to the total.
- For every franchisee whose total sales across all days is a multiple of 13, 
that multiple will be given as bonuses.
For example: 
a franchisee that sold a total of 39 baked goods will add 39 / 13 = 3 bonuses 
to the total.
Determine the total number of bonuses awarded.

Input

The input consists of 10 test cases. 
Each test case contains the following lines:
- A line containing the integer number of franchisees f
and integer number of days d, separated by a space. 
f is between 4 and 130, and d is between 2 and 4,745.
- d lines, one per day, containing f integers separated by
spaces. 
Each integer speciﬁes a number of sales. 
- The ﬁrst of these lines gives the sales for each franchise on
the ﬁrst day, 
- the second gives the sales for each franchise on the second day, and so on. 
Each integer is between 1 and 13,000.

Output

For each test case, output the total number of bonuses awarded.
"""

def get_bonuses_awarded(franchisees, days, *sales):
    bonuses = 0

    for i in range(franchisees):
        total = 0
        for sale in sales:
            sale = sale.split()
            total += int(sale[i])
        if total % 13 == 0:
            bonuses += total // 13
    
    for sale in sales:
        sales = [int(value) for value in sale.split()]
        if sum(sales) % 13 == 0:
            bonuses += sum(sales) // 13
    
    

    return bonuses


if __name__=='__main__':
    get_bonuses_awarded(4, 2, '4 5 1 3', '4 5 1 3')