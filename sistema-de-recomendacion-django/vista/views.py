from django.shortcuts import render
import recommended_util

from django.http import HttpResponse


# Create your views here.

def recomendaciones(request):
    # elementos random a mostrar:
    autores = recommended_util.recommendation_randomly_list(1)

    final_autor = []

    for a in autores:
        final_autor.append(str(a))
    # Query de busqueda

    # Query de prueba
    query = final_autor[0]

    recomendacion = recommended_util.recommend_util(query)
    recomendacion_final =[]
    for r in recomendacion:
        recomendacion_final.append(r)

    return render(request, 'index.html', {'autores': final_autor,'recomendaciones':recomendacion_final })
