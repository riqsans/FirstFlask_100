from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        nama = request.form.get('nama')
        umur = request.form.get('umur')
        
        if nama and umur:
            result = f"Halo {nama}, umur Anda adalah {umur} tahun."
        else:
            result = "Silakan isi semua field!"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)