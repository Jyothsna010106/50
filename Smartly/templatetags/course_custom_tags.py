from django import template
import math

register = template.Library()

#100 ->10% -->mrp - (mrp*discount*1/0.01) = saleprice
@register.simple_tag
def cal_sellprice(price,discount):
    if discount is None or discount== 0:
        return price 
    
        
    sellprice = price 
    sellprice=price-(price * discount * 0.01)
    return math.floor(sellprice)
        

@register.filter
def rupee(price):
    return f'₹{price}'