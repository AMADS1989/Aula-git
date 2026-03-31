import subprocess

def obter_mudancas_git():
    """Captura as mudanças que já foram adicionadas ao 'staging' (git add)."""
    try:
        # Executa o comando 'git diff --cached' para ver o que será commitado
        diff = subprocess.check_output(['git', 'diff', '--cached']).decode('utf-8')
        return diff
    except Exception as e:
        return f"Erro ao acessar o Git: {e}"

# 1. O Agente lê as mudanças reais do seu código
diff_do_codigo = obter_mudancas_git()

# 2. O Agente monta o 'Prompt' para enviar à IA
prompt_agente = f"""
Você é um Agente de IA especializado em Git. 
Analise o diff abaixo e sugira uma mensagem de commit seguindo o padrão 'Conventional Commits'.

DIFF:
{diff_do_codigo}
"""

print("Prompt preparado pelo Agente:")
print(prompt_agente)