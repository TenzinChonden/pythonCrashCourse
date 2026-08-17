def order_toppings(*toppings): 
    for topping in toppings: 
        print(f"You have added {topping} to your sandwich.")

order_toppings("Pepper")
order_toppings("pork", "bacon")
order_toppings("cheese", "salsa", "corn")
