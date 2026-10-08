from django.shortcuts import get_object_or_404, redirect, render

from .models import Asistencia
# Create your views here.


# CREAR
def crear(request):

    if request.method == "POST":

        asistencia = Asistencia(
            tipo_documento=request.POST["tipo_documento"],
            documento=request.POST["documento"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            whatsapp=request.POST["whatsapp"],
            fecha=request.POST["fecha"],
            asistio=request.POST.get("asistio") == "on"
        )

        asistencia.save()

    return render(request, "formulario.html")




# LISTAR
def listar(request):

    asistencias = Asistencia.objects.all()

    return render(
        request,
        "lista.html",
        {"asistencias": asistencias}
    )


# VER
def detalle(request, id):

    asistencia = get_object_or_404(Asistencia, id=id)

    return render(
        request,
        "detalle.html",
        {"asistencia": asistencia}
    )


# EDITAR
def editar(request, id):

    asistencia = get_object_or_404(Asistencia, id=id)

    if request.method == "POST":

        asistencia.tipo_documento = request.POST["tipo_documento"]
        asistencia.documento = request.POST["documento"]
        asistencia.nombre = request.POST["nombre"]
        asistencia.apellido = request.POST["apellido"]
        asistencia.whatsapp = request.POST["whatsapp"]
        asistencia.fecha = request.POST["fecha"]
        asistencia.asistio = request.POST.get("asistio") == "on"

        asistencia.save()

        return render(
            request,
            "detalle.html",
            {"asistencia": asistencia}
        )

    return render(
        request,
        "formulario.html",
        {"asistencia": asistencia}
    )



# ELIMINAR
def eliminar(request, id):

    Asistencia.objects.filter(id=id).delete()

    return redirect("/asistencia/lista/")