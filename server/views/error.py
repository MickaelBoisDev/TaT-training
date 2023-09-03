from django.shortcuts import render

from django.http import JsonResponse


def handler400(request, exception, template_name="400.html"):
    context = {}
    context["exception"] = exception
    return render(request, 'common/400.html', context, status=400)


def handler403(request, exception, template_name="403.html"):
    context = {}
    context["exception"] = exception
    return render(request, 'common/403.html', context, status=403)


def handler404(request, exception, template_name="404.html"):
    if "Authorization" in request.headers:
        return JsonResponse(data={
            'status': "NotFound",
            'err_msg': f"Incorrect URL {exception.args[0]['path']}"
        }, status=404)
    else:
        return render(request, 'common/404.html', status=404)


def handler500(request, template_name="500.html"):
    return render(request, 'common/500.html', status=500)
