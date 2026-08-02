
# importing nessary modules
import pandas as pd
import matplotlib.pyplot as plt

# SALES
def sales():
    while True:
        try:
            prodect_vareation=int(input('enter the varies of prodect sold accoding to price\n'))
            break

        except ValueError:
            print('you have entered a roung data type please enter a integer value\n')
            continue
           

    product=[]
    price=[]
    product_sales=[]

    for i in range(prodect_vareation):
        
        while True:
            prodect_name=input('enter the prodect name \n')

            if prodect_name.replace(" ","").isalpha():
                break
                
            else:
                print('you have entered a roung dtype please change it to character\n')
                continue
                
        
        
        
        
        
        while True:
            try:           
                price_of_product=int(input('enter the price of each prodect\n'))
                product_sold=int(input('enter the number of prodect sold \n'))
                break
                
                
            except ValueError:
                print('you have entered the roung value\n')
                continue

        product.append(prodect_name)
        price.append(price_of_product)
        product_sales.append(product_sold)

    return price, product_sales , product

    



# profit

def gross_profit ():

    while True:
        try:
            rs_per_month_gross=int(input('enter how how much month do you want to enter your revenue for opration , cost of revenue from opration\n'))
            break

        except ValueError:
            print('you have entered a roung datatype please enter a number\n')
            continue

    revenue_from_opration=[]
    cost_of_revenue_from_opration=[]

    for i in range (rs_per_month_gross):
        while True :
            try:
                revenue_From_opration=int(input('please enter your revenue from opration\n'))
                cost_Of_revenue_from_opration=int(input('please enter your cost of revenue from opration\n'))
                break

            except:
                print('you have entred the roumg dtype\n')
                continue


        revenue_from_opration.append(revenue_From_opration)
        cost_of_revenue_from_opration.append(cost_Of_revenue_from_opration)


    pd.Series(revenue_from_opration)
    pd.Series(cost_of_revenue_from_opration)
    return revenue_from_opration , cost_of_revenue_from_opration
    
    


def net_profit():
    while True:
        try:
            rs_per_month_net=int(input('enter how how much month do you want to enter your operating profit , non operating income , non operating expence\n'))
            break


        except ValueError:
            print('youhave entered the roung data type please enter a number\n')
            continue

    operating_profit=[]
    non_operating_expence=[]
    non_operating_income=[]

    for i in range (rs_per_month_net):
        while True:
            try:
                operating_Profit=int(input('enter your opperating profit\n'))
                non_Operating_expence=int(input('please enter your non operating expence\n'))
                non_operating_Income=int(input('enter your non operating income\n'))
                break



            except ValueError:
                print('you have entred roung dtype please enter character value\n')
                continue

        operating_profit.append(operating_Profit)
        non_operating_expence.append(non_Operating_expence)
        non_operating_income.append(non_operating_Income)
    pd.Series(operating_Profit)
    pd.Series(non_operating_expence)
    pd.Series(non_operating_income)

    return operating_profit , non_operating_income , non_operating_expence




#calculation


def sales_cal( price, product_sales,product):
    p=pd.Series(product_sales,index=product)
    pr=pd.Series(price,index=product)

    
    total_sales=(p*pr)
    print(total_sales)
    return p , pr , total_sales

price , product_sales , product=sales()
total=sales_cal(price , product_sales , product)





def gros_profit_cal(revenue_from_opration , cost_of_revenue_from_opration):
    gross_profits=pd.Series(revenue_from_opration)-pd.Series(cost_of_revenue_from_opration)
    print(gross_profits)

    return gross_profits





revenue_from_opration , cost_of_revenue_from_opration=gross_profit()

gros_profit_cal(revenue_from_opration , cost_of_revenue_from_opration)






def net_profit_cal(operating_profit , non_operating_income , non_operating_expence):
    net_profits=pd.Series(operating_profit)-pd.Series(non_operating_expence)+pd.Series(non_operating_income)
    print(net_profits)
    return net_profits



operating_profit , non_operating_income , non_operating_expence=net_profit()
toal=net_profit_cal(operating_profit , non_operating_income , non_operating_expence)




#report
def report_c():


    while True:
        report_i=input('enter yes for making a report enter q for not making a report\n')
        if report_i.replace('','').isalpha():
            break

        else:
            print('you have entered a roung dtype please enter a character\n')
            continue

    report_i=report_i.lower()


    return report_i   
        
        
def report_input(report_i):


    while report_i not in['yes','y','q']:
        while True:
            report_i=input(' you have putten a roung input please put one of this to contioune YES yes Y Y \n')
            report_i=report_i.lower()
        
        

            if report_i.replace(' ','').isalpha:
                break

            else:
                print('you have ebtered a roung data type please enter alfabets /n')
                continue
    return report_i



def report (p,pr,total_sales,product):
    annual_sales=pd.DataFrame({'no of product sold':p,'price':pr,'total sales':total_sales}, index=product)
    return annual_sales



    
def annual_report(annual_sales):
    print(annual_sales)



report_i=report_c()    
report_i = report_input(report_i)
if report_i in['yes','y']:
    while True:
        try:
            year=int(input('enter the current year \n'))
            break
            
        except ValueError:
            print('you have antred a roung dtype please enter a integer')
            continue




    p , pr , total_sales =sales_cal(price, product_sales,product)
    annual_sales = report(p, pr, total_sales , product)
    print(f'this is your sales report for the year {year}\n')

    annual_report(annual_sales)


def annual_report_profit(revenue_from_opration , cost_of_revenue_from_opration,operating_profit , non_operating_income , non_operating_expence):
    annual_profit=pd.DataFrame({'revenue  from opration':revenue_from_opration,'cost_of_revenue_from_opration':cost_of_revenue_from_opration,'operating_profit':operating_profit,'non_operating_income':non_operating_income,'non_operating_expence':non_operating_expence,'net profit':net_profit_cal,'gross profit':gros_profit_cal})

    return annual_profit

def output(annual_profit):
    print(f'this  is you annual report {annual_profit}')



# VISULATION


def visual_info():
    while True :
        visual_data=input('for sheeain a visual represation of sales enter yes in not intreated enter q\n')
        if visual_data.replace(' ','').isalpha():
            break
        else :
            print('you have putten a roung dtpe please fix it and you alfabet')
            continue




    visual_data=visual_data.lower()

    

    while visual_data not in['q','yes','y']:
        visual_data=input('please enter a valed input use yes YES y Y or q' )
    
    return visual_data
    


def visulation_of_sales(total_sales,product):
    
    plt.bar(product,total_sales,color='r')
    plt.grid()
    plt.title('the visual represtation of sales')
    plt.xlabel('price')
    plt.ylabel('producu')
    plt.legend()
    plt.show()

visual_data = visual_info()



if visual_data in['yes','y']:
    visulation_of_sales(total_sales,product)

elif visual_data =='q':
    quit()


def visulation_of_profit(gross_profits,net_profits):
    plt.plot(gross_profits, color='red', label='Gross Profit')
    plt.plot(net_profits, color='blue', label='Net Profit')
    plt.legend()
    plt.grid()
    plt.title('net profit & gross sales')
    plt.ylabel('net_profit')
    plt.xlabel('gross_profit')
    plt.show()

gross_profits=gros_profit_cal(revenue_from_opration , cost_of_revenue_from_opration)

net_profits = net_profit_cal(operating_profit , non_operating_income , non_operating_expence)

visulation_of_profit(gross_profits , net_profits)

if visual_data in['yes','y']:
    visulation_of_profit(gross_profits , net_profits)


elif visual_data =='q':
    quit()