import os, json

def fallback(description, location):
    t = description.lower()
    rules = [
      (['pothole','road damage','road broken'], 'Road Damage','High','High','Roads & Infrastructure'),
      (['streetlight','street light','light not working'], 'Streetlight','Medium','Medium','Electrical Department'),
      (['garbage','waste','trash','dump'], 'Garbage','Medium','Medium','Sanitation Department'),
      (['water leak','water leakage','pipe leak'], 'Water Leakage','High','High','Water Department'),
      (['drain','drainage','sewage'], 'Drainage','High','High','Sanitation Department'),
      (['footpath','sidewalk','pavement'], 'Damaged Footpath','Medium','Medium','Roads & Infrastructure')]
    for words,cat,sev,risk,dept in rules:
        if any(w in t for w in words):
            return {'category':cat,'severity':sev,'safety_risk':risk,'department':dept,
                    'summary':f'{cat} reported at {location}.',
                    'priority_reason':f'{sev} priority based on the described civic risk.',
                    'source':'Fallback analyzer'}
    return {'category':'Other Civic Issue','severity':'Medium','safety_risk':'Medium',
            'department':'Municipal Services','summary':f'Civic issue reported at {location}.',
            'priority_reason':'Requires municipal review.','source':'Fallback analyzer'}

def analyze_with_ai(description, location):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key: return fallback(description, location)
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        prompt = f'''Analyze this civic complaint for a municipal dashboard.\nLocation: {location}\nComplaint: {description}\nReturn ONLY valid JSON with keys: category, severity, safety_risk, department, summary, priority_reason. severity and safety_risk must be High, Medium, or Low. Choose practical departments such as Roads & Infrastructure, Sanitation Department, Water Department, Electrical Department, Parks Department, or Municipal Services.'''
        r = client.responses.create(model=os.getenv('OPENAI_MODEL','gpt-5-mini'), input=prompt)
        data = json.loads(r.output_text)
        required = ['category','severity','safety_risk','department','summary','priority_reason']
        if not all(k in data for k in required): raise ValueError('Incomplete AI response')
        data['source'] = 'OpenAI'
        return data
    except Exception:
        return fallback(description, location)
