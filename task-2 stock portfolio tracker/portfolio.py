print("=================================")
print("     STOCK PORTFOLIO TRACKER     ")
print("welcome to our stock portfolio tracker")
#use of dictionary TO STORE PORT FOLIO RECORDS
portfolio ={}
#loop is used to add multiple stocks in the portfolio
while True:
    stock_name=input("enter stock name:")
    quantity=int(input("enter quantity"))
    price=float(input("enter price per share:"))
    total_value = quantity * price
#stock_name works as a key for the portfolio dictionary 
    portfolio[stock_name]={
        "quantity":quantity,
        "price":price,
        "total_value":total_value
     }
    choice =input("do you want to add another stock! (yes/no): ")
    if choice.lower() != "yes":
       break
portfolio_total=0
for stock_name in portfolio:
    stock_data = portfolio[stock_name]
    portfolio_total +=stock_data["totalvalue"]
print("total porfolio value:",portfolio_total)
print("======THANK YOU======")
save_choice= input("do you want to save portfolio (yes/no): ")
if save_choice.lower() =="yes":
    with open("portfolio.txt","w") as file:
      file.write("STOCK PORTFOLIO SUMMARY\n")
      for stock_name in portfolio:
         stock_data=portfolio[stock_name]
         file.write

print("portfolio:",portfolio)
print("stock name:",stock_name)
print("quantity:",quantity)
print("price per share:",price)
print("total stock value",total_value)



