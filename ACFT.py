import mdlpoints as mdlp # utilizes the dictionary for maximum dead lift points
import sptpoints as sptp # utilizes the dictionary for standing power throw points
import hrppoints as hrpp # utilizes the dictionary for hand release pushup points
import sdcpoints as sdcp # utilizes the dictionary for sprint drag carry points
import plnkpoints as plnkp # utilizes the dictionary for the plank points
import tmrpoints as tmrp # utilizes the dictionary for the two mile run points
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

event_dicts = {
    'male': {
        '17-21': {
            'mdl': mdlp.mdl1721m_dict,
            'hrp': hrpp.hrp1721m_dict,
            'spt': sptp.spt1721m_dict,
            'sdc': sdcp.sdc1721m_dict,
            'plnk': plnkp.plnk1721_dict,
            'tmr': tmrp.tmr1721m_dict
        },
        '22-26': {
            'mdl': mdlp.mdl2226m_dict,
            'hrp': hrpp.hrp2226m_dict,
            'spt': sptp.spt2226m_dict,
            'sdc': sdcp.sdc2226m_dict,
            'plnk': plnkp.plnk2226_dict,
            'tmr': tmrp.tmr2226m_dict
        },
        '27-31': {
            'mdl': mdlp.mdl2731m_dict,
            'hrp': hrpp.hrp2731m_dict,
            'spt': sptp.spt2731m_dict,
            'sdc': sdcp.sdc2731m_dict,
            'plnk': plnkp.plnk2731_dict,
            'tmr': tmrp.tmr2731m_dict
        },
        '32-36': {
            'mdl': mdlp.mdl3236m_dict,
            'hrp': hrpp.hrp3236m_dict,
            'spt': sptp.spt3236m_dict,
            'sdc': sdcp.sdc3236m_dict,
            'plnk': plnkp.plnk3236_dict,
            'tmr': tmrp.tmr3236m_dict
        },
        '37-41': {
            'mdl': mdlp.mdl3741m_dict,
            'hrp': hrpp.hrp3741m_dict,
            'spt': sptp.spt3741m_dict,
            'sdc': sdcp.sdc3741m_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr3741m_dict
        },
        '42-46': {
            'mdl': mdlp.mdl4246m_dict,
            'hrp': hrpp.hrp4246m_dict,
            'spt': sptp.spt4246m_dict,
            'sdc': sdcp.sdc4246m_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr4246m_dict
        },
        '47-51': {
            'mdl': mdlp.mdl4751m_dict,
            'hrp': hrpp.hrp4751m_dict,
            'spt': sptp.spt4751m_dict,
            'sdc': sdcp.sdc4751m_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr4751m_dict
        },
        '52-56': {
            'mdl': mdlp.mdl5256m_dict,
            'hrp': hrpp.hrp5256m_dict,
            'spt': sptp.spt5256m_dict,
            'sdc': sdcp.sdc5256m_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr5256m_dict
        },
        '57-61': {
            'mdl': mdlp.mdl5761m_dict,
            'hrp': hrpp.hrp5761m_dict,
            'spt': sptp.spt5761m_dict,
            'sdc': sdcp.sdc5761m_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr5761m_dict
        },
        '62+': {
            'mdl': mdlp.mdl62m_dict,
            'hrp': hrpp.hrp62m_dict,
            'spt': sptp.spt62m_dict,
            'sdc': sdcp.sdc62m_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr62m_dict
        },
    },
    'female': {
        '17-21': {
            'mdl': mdlp.mdl1721f_dict,
            'hrp': hrpp.hrp1721f_dict,
            'spt': sptp.spt1721f_dict,
            'sdc': sdcp.sdc1721f_dict,
            'plnk': plnkp.plnk1721_dict,
            'tmr': tmrp.tmr1721f_dict
        },
        '22-26': {
            'mdl': mdlp.mdl2226f_dict,
            'hrp': hrpp.hrp2226f_dict,
            'spt': sptp.spt2226f_dict,
            'sdc': sdcp.sdc2226f_dict,
            'plnk': plnkp.plnk2226_dict,
            'tmr': tmrp.tmr2226f_dict
        },
        '27-31': {
            'mdl': mdlp.mdl2731f_dict,
            'hrp': hrpp.hrp2731f_dict,
            'spt': sptp.spt2731f_dict,
            'sdc': sdcp.sdc2731f_dict,
            'plnk': plnkp.plnk2731_dict,
            'tmr': tmrp.tmr2731f_dict
        },
        '32-36': {
            'mdl': mdlp.mdl3236f_dict,
            'hrp': hrpp.hrp3236f_dict,
            'spt': sptp.spt3236f_dict,
            'sdc': sdcp.sdc3236f_dict,
            'plnk': plnkp.plnk3236_dict,
            'tmr': tmrp.tmr3236f_dict
        },
        '37-41': {
            'mdl': mdlp.mdl3741f_dict,
            'hrp': hrpp.hrp3741f_dict,
            'spt': sptp.spt3741f_dict,
            'sdc': sdcp.sdc3741f_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr3741f_dict
        },
        '42-46': {
            'mdl': mdlp.mdl4246f_dict,
            'hrp': hrpp.hrp4246f_dict,
            'spt': sptp.spt4246f_dict,
            'sdc': sdcp.sdc4246f_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr4246f_dict
        },
        '47-51': {
            'mdl': mdlp.mdl4751f_dict,
            'hrp': hrpp.hrp4751f_dict,
            'spt': sptp.spt4751f_dict,
            'sdc': sdcp.sdc4751f_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr4751f_dict
        },
        '52-56': {
            'mdl': mdlp.mdl5256f_dict,
            'hrp': hrpp.hrp5256f_dict,
            'spt': sptp.spt5256f_dict,
            'sdc': sdcp.sdc5256f_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr5256f_dict
        },
        '57-61': {
            'mdl': mdlp.mdl5761f_dict,
            'hrp': hrpp.hrp5761f_dict,
            'spt': sptp.spt5761f_dict,
            'sdc': sdcp.sdc5761f_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr5761f_dict
        },
        '62+': {
            'mdl': mdlp.mdl62f_dict,
            'hrp': hrpp.hrp62f_dict,
            'spt': sptp.spt62f_dict,
            'sdc': sdcp.sdc62f_dict,
            'plnk': plnkp.plnk3762_dict,
            'tmr': tmrp.tmr62f_dict
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_acft', methods=['POST'])
def handle_calculate_acft():
    try:
        data = request.get_json()
        acft_score = calculate_acft_score(data)
        response_data = {'acft_score': acft_score}
        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': 'An error occurred while calculating the ACFT score: ' + str(e)}), 400

def calculate_acft_score(data):
    age = data['age']
    gender = data['gender']
    mdl = int(data['mdl'])
    hrp = int(data['hrp'])
    spt = float(data['spt'])
    sdc_input = data['sdc']
    plnk_input = data['plnk']
    tmr_input = data['tmr']
#Print for troubleshooting
    print("Received gender:", gender)  
    print("Received age:", age)        
    print("Received mdl:", mdl)  
    print("Received hrp:", hrp)       
    print("Received spt:", spt)
    print("Received sdc:", sdc_input)
    print("Received plnk:", plnk_input)
    print("Received tmr:", tmr_input)        

    event_scores = event_dicts.get(gender, {}).get(age, {})
    mdl_points = event_scores.get('mdl', {}).get(mdl, 0)
    hrp_points = event_scores.get('hrp', {}).get(hrp, 0)
    spt_points = event_scores.get('spt', {}).get(spt, 0)
    sdc_points = event_scores.get('sdc', {}).get(sdc_input, 0)
    plnk_points = event_scores.get('plnk', {}).get(plnk_input, 0)
    tmr_points = event_scores.get('tmr', {}).get(tmr_input, 0)

    if None in [mdl_points, hrp_points, spt_points, sdc_points, plnk_points, tmr_points]:
        return 'Invalid input for one or more events'

    acft_score = mdl_points + hrp_points + spt_points + sdc_points + plnk_points + tmr_points

    if isinstance(acft_score, int):
        acft_score = int(acft_score)

    return acft_score

if __name__ == '__main__':
    app.run(debug=True)

      


