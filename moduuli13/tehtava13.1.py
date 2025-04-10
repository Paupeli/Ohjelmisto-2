from flask import Flask

app = Flask (__name__)

def is_prime(num):
    flag = True

    if num <2:
        flag = False
    else:
        for _ in range(2,num):
            if num % _ == 0:
                flag = False
                break
    return flag

@app.route('/prime_number/<int:number>', methods=['GET'])

def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return result

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)



