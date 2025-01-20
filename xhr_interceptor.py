from selenium import webdriver
from selenium.webdriver.common.by import By
import json

def intercept_xhr():
    driver = webdriver.Chrome()
    driver.get('https://gisweb.miamidade.gov/buildingreport/')
    
    script = """
    var xhrData = [];
    var _open = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function() {
        this.addEventListener('load', function() {
            xhrData.push({
                url: this.responseURL,
                data: this.response
            });
        });
        return _open.apply(this, arguments);
    }
    return xhrData;
    """
    
    driver.execute_script(script)
    return driver