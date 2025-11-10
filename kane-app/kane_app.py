import streamlit as st
import pandas as pd
import altair as alt # Precisamos disso para o gráfico de dispersão

# --- Dados ---
data = [
    {"Adversário": "Stuttgart", "Chutes": 2, "Chutes ao gol": 2, "Gols": 1, "Ass.": 0, "Passes": 28, "Passes completos": 21, "Minutos": 90},
    {"Adversário": "Leipzig", "Chutes": 5, "Chutes ao gol": 4, "Gols": 3, "Ass.": 0, "Passes": 29, "Passes completos": 23, "Minutos": 85},
    {"Adversário": "Wehen", "Chutes": 8, "Chutes ao gol": 6, "Gols": 2, "Ass.": 0, "Passes": 25, "Passes completos": 20, "Minutos": 90},
    {"Adversário": "Augsburg", "Chutes": 0, "Chutes ao gol": 0, "Gols": 0, "Ass.": 2, "Passes": 22, "Passes completos": 19, "Minutos": 90},
    {"Adversário": "Hamburgo", "Chutes": 2, "Chutes ao gol": 2, "Gols": 2, "Ass.": 1, "Passes": 27, "Passes completos": 23, "Minutos": 63},
    {"Adversário": "Chelsea", "Chutes": 5, "Chutes ao gol": 3, "Gols": 2, "Ass.": 0, "Passes": 25, "Passes completos": 21, "Minutos": 90},
    {"Adversário": "Hoffenheim", "Chutes": 6, "Chutes ao gol": 4, "Gols": 3, "Ass.": 0, "Passes": 30, "Passes completos": 26, "Minutos": 90},
    {"Adversário": "Werder Bremen", "Chutes": 6, "Chutes ao gol": 5, "Gols": 2, "Ass.": 0, "Passes": 19, "Passes completos": 15, "Minutos": 77},
    {"Adversário": "Pafos", "Chutes": 5, "Chutes ao gol": 3, "Gols": 2, "Ass.": 0, "Passes": 29, "Passes completos": 25, "Minutos": 63},
    {"Adversário": "Frankfurt", "Chutes": 2, "Chutes ao gol": 1, "Gols": 1, "Ass.": 0, "Passes": 23, "Passes completos": 17, "Minutos": 84},
    {"Adversário": "Dortmund", "Chutes": 2, "Chutes ao gol": 1, "Gols": 1, "Ass.": 0, "Passes": 48, "Passes completos": 38, "Minutos": 90},
    {"Adversário": "Brugge", "Chutes": 6, "Chutes ao gol": 3, "Gols": 1, "Ass.": 0, "Passes": 30, "Passes completos": 27, "Minutos": 68},
    {"Adversário": "Monchengladbach", "Chutes": 6, "Chutes ao gol": 2, "Gols": 0, "Ass.": 0, "Passes": 19, "Passes completos": 18, "Minutos": 90},
    {"Adversário": "Koln", "Chutes": 5, "Chutes ao gol": 3, "Gols": 2, "Ass.": 0, "Passes": 26, "Passes completos": 20, "Minutos": 86},
    {"Adversário": "Leverkusen", "Chutes": 1, "Chutes ao gol": 0, "Gols": 0, "Ass.": 0, "Passes": 10, "Passes completos": 9, "Minutos": 32},
    {"Adversário": "PSG", "Chutes": 1, "Chutes ao gol": 1, "Gols": 0, "Ass.": 0, "Passes": 23, "Passes completos": 12, "Minutos": 87},
    {"Adversário": "Union Berlin", "Chutes": 4, "Chutes ao gol": 1, "Gols": 1, "Ass.": 0, "Passes": 31, "Passes completos": 27, "Minutos": 90}
]

# Dados da linha "TOTAIS"
totals_data = {
    "Gols": 23, "Ass.": 3, "Chutes": 66, "Chutes ao gol": 41, 
    "Passes": 444, "Passes completos": 361, "Minutos": 1365
}

# --- Preparação do DataFrame ---
df = pd.DataFrame(data)
df.rename(columns={"Ass.": "Assistências"}, inplace=True)
df['% Passes Completos'] = (df['Passes completos'] / df['Passes'].apply(lambda x: x if x > 0 else 1)) * 100
total_pass_pct = (totals_data['Passes completos'] / totals_data['Passes']) * 100

# --- 2. Título e Logo ---
col1, col2 = st.columns([3, 1]) 

with col1:
    st.title("Painel de Estatísticas de Harry Kane")

# --- 3. Visão Geral (Totais) ---
st.header("Visão Geral (Totais)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Gols", totals_data['Gols'])
col2.metric("Assistências", totals_data['Ass.'])
col3.metric("Minutos", totals_data['Minutos'])

st.divider()
col5, col6 = st.columns(2)
with col5:
    st.subheader("Chutes")
    c5_1, c5_2 = st.columns(2)
    c5_1.metric("Chutes", totals_data['Chutes'])
    c5_2.metric("Chutes ao Gol", totals_data['Chutes ao gol'])
with col6:
    st.subheader("Passes")
    c6_1, c6_2, c6_3 = st.columns(3)
    c6_1.metric("Passes", totals_data['Passes'])
    c6_2.metric("Passes Completos", totals_data['Passes completos'])
    c6_3.metric("% Passes Completos", f"{total_pass_pct:.1f}%")

# --- 4. Filtro por Adversário (na Barra Lateral) ---
st.sidebar.header("Filtros")
opponent_list = df['Adversário'].unique()
selected_opponent = st.sidebar.selectbox(
    "Selecione o Adversário:",
    opponent_list
)

# --- 5. Métricas do Adversário Selecionado ---
st.divider()
st.header(f"Números contra: {selected_opponent}")
game_data = df[df['Adversário'] == selected_opponent].iloc[0]
g_col1, g_col2, g_col3 = st.columns(3)
g_col1.metric("Gols", game_data['Gols'])
g_col2.metric("Assistências", game_data['Assistências'])
g_col3.metric("Minutos", f"{game_data['Minutos']} min")
s_col1, s_col2 = st.columns(2)
s_col1.metric("Chutes", game_data['Chutes'])
s_col2.metric("Chutes ao Gol", game_data['Chutes ao gol'])
p_col1, p_col2, p_col3 = st.columns(3)
p_col1.metric("Passes", game_data['Passes'])
p_col2.metric("Passes Completos", game_data['Passes completos'])
p_col3.metric("% Passes Completos", f"{game_data['% Passes Completos']:.1f}%")

# --- 6. SUGESTÕES DE GRÁFICOS ---
st.divider()
st.header("Análise Gráfica")

# --- Exemplo 1: Gráfico de Barras (Comparação de Chutes e Gols) ---
st.subheader("Comparação: Gols, Chutes e Chutes ao Gol")
st.write("Este gráfico mostra a eficiência: o total de chutes e quantos viraram chutes ao gol ou gols.")
df_gols_chutes = df.set_index('Adversário')
st.bar_chart(df_gols_chutes[['Gols', 'Chutes ao gol', 'Chutes']])

# --- Exemplo 2: Gráfico de Linha (Performance de Passes) ---
st.subheader("Performance de Passes por Jogo")
st.write("Aqui vemos a consistência dos passes ao longo dos jogos.")
df_passes = df.set_index('Adversário')
st.line_chart(df_passes[['Passes', 'Passes completos']])

# --- Exemplo 3: Gráfico de Dispersão (COM ZOOM CORRIGIDO) ---
st.subheader("Relação: Minutos Jogados vs. Gols")
st.write("Este gráfico ajuda a ver se há uma correlação entre jogar mais minutos e marcar mais gols.")

# O Altair vai detectar o config.toml e usar o tema escuro
scatter_chart = alt.Chart(df).mark_circle(size=70).encode(
    x=alt.X('Minutos', scale=alt.Scale(domain=[0, df['Minutos'].max() + 10])),
    y=alt.Y('Gols', scale=alt.Scale(domain=[-0.5, df['Gols'].max() + 1])),
    
    # <--- MUDANÇA AQUI ---
    # Forçamos o uso da paleta 'tableau20' (que tem 20 cores)
    # para garantir que cada time tenha uma cor única.
    color=alt.Color('Adversário', scale=alt.Scale(scheme='tableau20')), 
    
    tooltip=['Adversário', 'Minutos', 'Gols', 'Assistências'] 
).properties(
    title="Minutos vs. Gols"
).interactive() # Adicionei .interactive() para permitir zoom e pan

st.altair_chart(scatter_chart, use_container_width=True)

# Opcional: Mostrar a tabela de dados completa
with st.expander("Ver tabela de dados completa"):
    st.dataframe(df.set_index('Adversário'))