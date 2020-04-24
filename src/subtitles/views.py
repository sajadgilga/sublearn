from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from subtitles.services import process_sub
from mimetypes import guess_type
@login_required
def sub_processor(request):
    if request.method == 'POST' and ('subtitle' in request.FILES):
        uploaded_sub = request.FILES['subtitle']
        name = uploaded_sub.name
        type = name[name.rfind('.'):]
        text = uploaded_sub.read().decode('iso-8859-1')
        result = process_sub(text, type, 3)
        for word in result.keys():
            replacement = "{0} ({1})".format(word, result[word][0])
            text = text.replace(word, replacement)
            print(replacement)
        filename = name[:name.rfind('.')] + "enchanted" + type
        content = text.encode('utf-8')
        response = HttpResponse(content, content_type=guess_type(filename))
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response


        # print(text)

    return render(request, 'subtitles/upload.html')

