day = input("Enter day:")


def calculation_ama(selling_price,pauk):
    commission = selling_price*(5/100)
    cor_sell = selling_price-commission
    final= cor_sell-(80*pauk)
     
    return final
def calculation_MT(selling_price,pauk):
    commission = selling_price*(14/100)
    cor_sell = selling_price-commission
    final= cor_sell-(80*pauk)
    
    return final

def calculation_Nan(selling_price,pauk):
    commission = selling_price*(14/100)
    cor_sell = selling_price-commission
    final= cor_sell-(80*pauk)
    
    return final

def calculation_Anty(selling_price,pauk):
    commission = selling_price*(12/100)
    cor_sell = selling_price-commission
    final= cor_sell-(80*pauk)
    
    return final

user1 = input('ama:')
selling_price_ama = int(input("selling price_Ama:"))
pauk_ama = int(input("p_Ama:"))
user2= input('mt:')

selling_price_MT = int(input("selling price_MT:"))
pauk_MT = int(input("p_MT:"))
user3 = input('nan:')

selling_price_Nan = int(input("selling price_Nan:"))
pauk_Nan = int(input("p_Nan:"))
user4= input('anty:')

selling_price_Anty = int(input("selling price_Anty:"))
pauk_Anty = int(input("p_Anty:"))

final_ama = calculation_ama(selling_price_ama,pauk_ama)
final_MT = calculation_ama(selling_price_MT,pauk_MT)

final_Nan = calculation_ama(selling_price_Nan,pauk_Nan)

final_Anty = calculation_ama(selling_price_Anty,pauk_Anty)
#print(final)
#final = calculation_ama(selling_price_ama,pauk_ama)

if final_ama>=0:
    print(f"{day}\n{selling_price_ama}\np{pauk_ama}\nAma total=+{final_ama}\n")
else:
    print(f"{day}\n{selling_price_ama}\np{pauk_ama}\nAma total={final_ama}\n")

if final_MT>=0:
    print(f"{day}\n{selling_price_MT}\np{pauk_MT}\nMT total=+{final_MT}\n")
else:
    print(f"{day}\n{selling_price_MT}\np{pauk_MT}\nMT total={final_MT}\n")
if final_Nan>=0:    
    print(f"{day}\n{selling_price_Nan}\np{pauk_Nan}\nNan total=+{final_Nan}\n")
else:
    print(f"{day}\n{selling_price_Nan}\np{pauk_Nan}\nNan total={final_Nan}\n")
if final_Anty>=0:
    print(f"{day}\n{selling_price_Anty}\np{pauk_Anty}\nAnty total=+{final_Anty}\n")
else:
    print(f"{day}\n{selling_price_Anty}\np{pauk_Anty}\nAnty total={final_Anty}\n")


"""if final>=0:
    print(f"{day}\n16%={selling_price_16}/{pauk_16}\n+{final}")
else:
    print(f"{day}\n16%={selling_price_16}/{pauk_16}\n{final}")
        
final_2 = calculation_2(selling_price_18,pauk_18)
#print(final_2) 

if final_2>=0:
    print(f"18%={selling_price_18}/{pauk_18}\n+{final_2}")
else:
    print(f"18%={selling_price_18}/{pauk_18}\n{final_2}")
total = final+final_2
me = total *(4/100)
print(f"total = {total}\n4%={int(me)}")"""
