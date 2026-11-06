import streamlit as st

st.header('Lanzar una moneda')

chart = st.empty()

def toss_coin(n): #Función que simula el lanzamiento de una moneda
	trial_outcomes = scipy.stats.bernoulli.rvs(p = 0.5, size = n)
	mean = None
	outcome_no = 0
	outcome_1_count = 0
	means = []

	for r in trial_outcomes:
		outcome_no += 1
		if r == 1:
			outcome_1_count += 1
		mean outcome_1_count / outcome_no
		means.append(mean)
		char.line_chart(means)
		time.sleep(0.05)
	return mean

number_of_trials = st.slider('¿Número de intentos?', 1, 100, 10)
start_button = st.button('Ejecutar')

if start_button:
	st.write(f'Experimento con {number_of_trials} intentos en curso')
	mean = toss_coin(number of trials)
