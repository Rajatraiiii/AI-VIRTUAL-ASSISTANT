from requests_html import HTMLSession

def Weather():
    try:
        s  = HTMLSession()
        query = "patna"
        url = f'https://www.google.com/search?q=weather+{query}'
        r  = s.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        })

        temp_elem = r.html.find('span#wob_tm', first=True)
        unit_elem = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
        desc_elem = r.html.find('span#wob_dc', first=True)

        if temp_elem and unit_elem and desc_elem:
            temp = temp_elem.text
            unit = unit_elem.text
            desc = desc_elem.text
            return f"{temp}°{unit}, {desc}"
        else:
            return "Sorry, could not fetch the weather information from Google."

    except Exception as e:
        return f"Error fetching weather: {e}"
