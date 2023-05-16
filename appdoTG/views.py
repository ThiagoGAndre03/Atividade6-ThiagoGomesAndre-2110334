from django.shortcuts import render, redirect  # Importa funções utilitárias do Django para renderização de templates e redirecionamento de URLs
from .models import TiquinhoStats  # Importa o modelo TiquinhoStats do arquivo models.py
from .models import TiquinhoTeams  # Importa o modelo TiquinhoTeams do arquivo models.py

# Função de visualização para a página de atividade1
def atividade1(request):
    return render(request, "atividade1.html")  # Renderiza o template 'atividade1.html'

# Função de visualização para listar as estatísticas (TiquinhoStats)
def list_stats(request):
    stats = TiquinhoStats.objects.all()  # Obtém todos os objetos do modelo TiquinhoStats do banco de dados
    context = {"stats": stats}  # Define o contexto com a variável 'stats' contendo os objetos obtidos
    return render(request, "list_stats.html", context=context)  # Renderiza o template 'list_stats.html' com o contexto

# Função de visualização para listar as equipes (TiquinhoTeams)
def list_teams(request):
    teams = TiquinhoTeams.objects.all()  # Obtém todos os objetos do modelo TiquinhoTeams do banco de dados
    context = {"teams": teams}  # Define o contexto com a variável 'teams' contendo os objetos obtidos
    return render(request, "list_teams.html", context=context)  # Renderiza o template 'list_teams.html' com o contexto

# Função de criação de estatísticas (TiquinhoStats)
def create_stats(request):
    if request.method == "POST":
        TiquinhoStats.objects.create(
            título=request.POST["título"],
            números=request.POST["números"],
            tipo=request.POST["tipo"],
            essa_temporada=False
        )
        return redirect("stats-list")  # Redireciona para a página de listagem de estatísticas após a criação

    return render(request, "stats_form.html")  # Renderiza o formulário de criação de estatísticas

# Função de criação de equipes (TiquinhoTeams)
def create_teams(request):
    if request.method == "POST":
        TiquinhoTeams.objects.create(
            título=request.POST["título"],
            time=request.POST["time"],
            gols=request.POST["gols"],
            clube_atual=False
        )
        return redirect("teams-list")  # Redireciona para a página de listagem de equipes após a criação

    return render(request, "team_forms.html")  # Renderiza o formulário de criação de equipes

# Função para excluir estatísticas (TiquinhoStats)
def delete_stats(request, stats_id):
    stats = TiquinhoStats.objects.get(id=stats_id)  # Obtém o objeto TiquinhoStats com o ID fornecido
    if request.method == 'POST':
        if "confirm" in request.POST:
            stats.delete()  # Exclui o objeto TiquinhoStats
            return redirect('stats-list')  # Redireciona para a página de listagem de estatísticas após a exclusão
    return render(request, "list_stats.html", context={"stats": stats})  # Renderiza o template 'list_stats.html' com o contexto

# Funçãopara excluir times/gols (TiquinhoTeams)
def delete_teams(request, teams_id):
    teams = TiquinhoTeams.objects.get(id=teams_id)  # Obtém o objeto TiquinhoTeams com o ID fornecido
    if request.method == 'POST':
        if "confirm" in request.POST:
            teams.delete()  # Exclui o objeto TiquinhoTeams
            return redirect('teams-list')  # Redireciona para a página de listagem de equipes após a exclusão
    return render(request, "list_teams.html", context={"teams": teams})  # Renderiza o template 'list_teams.html' com o contexto

def edit_stats(request, stats_id):
    stats = TiquinhoStats.objects.get(id=stats_id)  # Obtém o objeto TiquinhoStats com o ID fornecido
    if request.method == 'POST':
        stats.título = request.POST["título"]
        stats.números = request.POST["números"]
        stats.tipo = request.POST["tipo"]
        stats.essa_temporada = False
        stats.save()  # Salva as alterações no objeto TiquinhoStats
        return redirect('stats-list')  # Redireciona para a página de listagem de estatísticas após a edição
    return render(request, "list_stats.html", context={"stats": stats})  # Renderiza o template 'list_stats.html'

def edit_teams(request, teams_id):
    teams = TiquinhoTeams.objects.get(id=teams_id)  # Obtém o objeto TiquinhoTeams com o ID fornecido
    if request.method == 'POST':
        teams.título = request.POST["título"]
        teams.time = request.POST["time"]
        teams.gols = request.POST["gols"]
        teams.clube_atual = False
        teams.save()  # Salva as alterações no objeto TiquinhoTeams
        return redirect('teams-list')  # Redireciona para a página de listagem de equipes após a edição
    return render(request, "list_teams.html", context={"teams": teams})  # Renderiza o template 'list_teams.html'
