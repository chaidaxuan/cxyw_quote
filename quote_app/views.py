from django.http import JsonResponse
from .models import Quote
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_quote(request):
    if request.method == 'POST':
        material = request.POST.get('material')
        size = request.POST.get('size')
        units = int(request.POST.get('units'))
        paper_sequence = request.POST.get('paper_sequence')
        pages_per_book = int(request.POST.get('pages_per_book'))
        printing_requirement = request.POST.get('printing_requirement')
        gluing_method = request.POST.get('gluing_method')
        quantity = int(request.POST.get('quantity'))

        quote = Quote(
            material=material,
            size=size,
            units=units,
            paper_sequence=paper_sequence,
            pages_per_book=pages_per_book,
            printing_requirement=printing_requirement,
            gluing_method=gluing_method,
            quantity=quantity
        )

        price = quote.calculate_price()

        return JsonResponse({'price': price})

    return JsonResponse({'error': 'Invalid request method'}, status=400)