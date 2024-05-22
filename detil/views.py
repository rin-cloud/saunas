from django.shortcuts import render
 
def detil_template(request):
    data = {
        "waterEvaluation":3,
        "saunaEvaluation":4,
        "inOutEvaluation":5,
        "access":"徒歩8分",
        "saunaThoughts":"最高",
        "saunaNice":"1",
        "comments":[
                        {
                            "comment":"いいね"
                        },
                        {
                            "comment":"やばい"
                        }
                    ]    
    }
    return render(request, 'detil.html',data)