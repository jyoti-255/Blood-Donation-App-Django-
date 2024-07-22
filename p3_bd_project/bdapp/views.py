from django.shortcuts import render
from .forms import BdForm

def home(request):
    if request.method=="POST":
           na=request.POST.get("name")
           ag=int(request.POST.get("age"))
           wt=float(request.POST.get("weight"))
        
           if(25<=ag<=40)and (40<=wt<=60):
               msg="Yes you can donate" 
           else:    
               msg="No you cannot donate"
           
           fm=BdForm(initial={"name":na,"age":ag,"weight":wt})
           return render(request,"home.html",{"fm":fm,"msg":msg})



    else:
         fm=BdForm()
         return render(request,"home.html",{"fm":fm})
 
      
