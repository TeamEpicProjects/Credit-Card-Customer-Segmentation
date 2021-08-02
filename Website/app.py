import numpy as np
from flask import Flask, request,  render_template
import pickle

app = Flask(__name__)
Model_One = pickle.load(open('ModelOne.pkl', 'rb'))
Model_Second = pickle.load(open('ModelTwo.pkl', 'rb'))
Model_Third = pickle.load(open('ModelThree.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = Model_One.predict(final_features)
    
    if prediction[0] == 0 :
        cluster = 'These customers mostly take cash advance, and do not use their credit card regularly. They maintain good balance. They must be encouraged to use their card more frequently'
    elif prediction[0] == 1 :
        cluster = 'These customers are low spenders, despite having a decent credit limit. But maintain very low balance. They usage of credit card is very minimal.They must encourage to transact more.'
    elif prediction[0] == 2 :
        cluster = 'This cluster does the maximum transactions with the credit card, they don’t cross their limit and also make payments to the bank. They take very less cash advance. This is a very good cluster of customers, and they must be given offers and incentives, to retain them.'
    else :
        cluster = 'These customers maintain very low balance, and all their transactions are proportional to their balance, despite a good credit limit. They must be encouraged to spend more, and must be targeted using offers and promotions.'
    
    return render_template('index.html', prediction_ModelOne=f'This customer belongs to cluster {prediction[0]}',InsightOne=cluster)

@app.route('/ModelSecond',methods=['POST'])
def ModelSecond():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = Model_Second.predict(final_features)

    if prediction[0] == 0 :
        cluster = 'These customers do very less transaction with their credit card, and mostly prefer cash advance, but they maintain good balance in their account, despite the cash advance, and also make significant payments. But they do not cross the credit limit. These customers need to be encouraged to transact more with their credit card.'
    elif prediction[0] == 1 :
        cluster = 'These customers have the highest credit limit compared to others, and they also tend to make transactions, beyond their limit. But they have also paid all their credit amount as seen from the graph. They are good customers as they spend more, use credit card regularly for one-off and installment purchases and also pay the credit amount back even though they cross their credit limit. And they do not take much cash advance.'
    elif prediction[0] == 2 :
        cluster = 'These customers have a high credit limit, and do not spend beyond their credit limit. They also do significant transactions with the credit card. And take very less cash advance. These customers are ideal customers and must be encouraged to transact more, as they do not make full use of their credit limit.'
    else :
        cluster = 'These customers are low spenders, despite having a good credit limit. But maintain very low balance. They usage of credit card is very minimal. They must encourage to transact more.'
 
    return render_template('index.html', prediction_ModelSecond=f'This customer belongs to cluster {prediction[0]}',InsightSecond=cluster)


@app.route('/ModelThird',methods=['POST'])
def ModelThird():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = Model_Third.predict(final_features)
    
    if prediction[0] == 0 :
        cluster = 'They are ideal customers, where their total transactions never crosses, the credit limit, and they payment is also up to the mark, they usually spend on both one off purchases and installments, they are an ideal group of customers, and we must do dome promotional activities so that they spend more'
    elif prediction[0] == 1 :
        cluster = 'These are customers, who maintain good balance and their transaction is usually proportion to their balance, they don’t cross the credit limit, and they have returned significant portion of their, credit value. They usually pay their credit amount in much lesser transactions than other customers. Hence, they are also an ideal set of customers, we must reach out to, so that they can do more transactions.'
    elif prediction[0] == 2 :
        cluster = 'They are low spenders, they usually maintain low balance and their purchase and spending depends on their balance'
    else :
        cluster = 'These are the customers who have a high credit limit, and tend to cross their credit limits, but they also make significant payments to their account, they usually spend for one off purchases. Hence, they are high spenders, and they also maintain good balance compared to other clusters. but we must be careful as they cross their credit limit.'
    
    return render_template('index.html', prediction_ModelThird=f'This customer belongs to cluster {prediction[0]}',InsightThird=cluster)


if __name__ == "__main__":
    app.run(debug=True)