from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 's3cr3t'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            height = request.form['height']
            weight = request.form['weight']
            
            if not height or not weight:
                flash('Por favor, preencha todos os campos.', 'error')
                return redirect(url_for('index'))
            
            height = float(height)
            weight = float(weight)

            if height <= 0 or weight <= 0:
                flash('A altura e o peso devem ser maiores que zero.', 'error')
                return redirect(url_for('index'))

            bmi = weight / (height / 100) ** 2

            if bmi < 18.5:
                category = 'Abaixo do peso'
            elif 18.5 <= bmi < 24.9:
                category = 'Peso normal'
            elif 25 <= bmi < 29.9:
                category = 'Sobrepeso'
            else:
                category = 'Obesidade'

            result = f"IMC: {bmi:.2f} - Categoria: {category}"

            if 'history' not in app.config:
                app.config['history'] = []
            app.config['history'].append(f"Altura: {height} cm, Peso: {weight} kg - {result}")

            return render_template('index.html', result=result, history=app.config['history'])

        except ValueError:
            flash('Por favor, insira valores válidos para altura e peso.', 'error')
            return redirect(url_for('index'))

    return render_template('index.html', result=None, history=app.config.get('history', []))


if __name__ == '__main__':
    app.run(debug=True)
