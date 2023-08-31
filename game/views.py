from django.shortcuts import render
from .forms import WordForm
from .models import Words
from .src.game.c_or_s import COrS

valid_words = list(Words.objects.values_list('word', flat=True))
game = COrS(valid_words)

def home(request):
    system_entry = game.get_latest_word_by_type("system")
    if not system_entry:
        system_entry = "cimento"
        game.add("system", system_entry)

    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            user_entry = form.cleaned_data['user_entry']
            if game.is_valid(user_entry):
                game.add("user", user_entry)
                system_entry = game.get_similar_word(user_entry)
                game.add("system", system_entry)



    return render(request, "base.html", {"system_entry": system_entry})