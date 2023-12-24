#STOCK IN PROJECT 
import os 
os.system('cls')
options=''
stocklist=[]
option_1=''
while True:
    options= input('>')
    if options == 'it':
        items=''
        while True:
            items = input('>>')
            stocklist.append(f'{items} =[]')
            if items == 'done':                
                break
            
    elif options == 'out':
        del stocklist[-1]
        print(stocklist)
        break
    elif options == 'ie':
        
        while True:
            option_1=input('>>>')
            if option_1 in stocklist:
                while True:
                    barcodes=input('>>>>')
                    option_1.append(barcodes)
                    if barcodes =='out':
                        del option_1[-1]
                        print(barcodes)
                        break
            elif option_1 not in stocklist:
                pass
            elif option_1 =="out":
                break
            else:
                pass

            
        
    else:
        print('follow instrutions \nitems_types \nout')
        