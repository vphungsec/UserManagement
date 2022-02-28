const DATE_FORMAT = 'DD/MM/YYYY';

function parseIntValue(value) {
  var parsed = parseInt(value);
  if (!isNaN(parsed) && parsed >= 0) {
    return parsed;
  }
  return null;
}

function parseJSON(str) {
  try {
    return JSON.parse(str)
  } catch (err) {
    return null;
  }
}

function isInteger(value) {
  try {
    var floatValue = parseFloat(value);
    return isFinite(floatValue) && Math.floor(floatValue) === floatValue;
  }
  catch (error) {
    return false;
  }
}

function isNullOrUndefined(value) {
  return _.isNull(value) || _.isUndefined(value);
}

ko.extenders.positiveInt = function (target) {
  var result = ko.pureComputed({
    read: target,
    write: function (newValue) {
      var intValue = parseIntValue(newValue);
      target(intValue);
      target.notifySubscribers(intValue);
    }
  }).extend({notify: 'always'});

  result(target());

  return result;
};

ko.extenders.trimmedString = function (target) {
  return ko.pureComputed({
    read: target,
    write: function (newValue) {
      if (newValue) {
        var trimmed = newValue.trim();
        target(trimmed);
        target.notifySubscribers(trimmed);
      }
      else target(newValue);
    }
  }).extend({notify: 'always'});
};

ko.bindingHandlers.fileUpload = {
  init: function (element, valueAccessor) {
    $(element).change(function () {
      valueAccessor()(element.files[0]);
    });
  },
  update: function (element, valueAccessor) {
    if (ko.unwrap(valueAccessor()) === null) {
      $(element).wrap('<form>').closest('form').get(0).reset();
      $(element).unwrap();
    }
  }
};

function getCSRFToken() {
  var $token = $('[name="csrfmiddlewaretoken"]')[0];
  return $token ? $token.value : '';
}

function jsonOrThrow(res) {
  if (!res.ok) throw new Error();
  return res.json();
}


function decodeNameWithHash(name) {
    return unescape(name).replace(/%2B/g, '+');
}

function encodeNameWithHash(name) {
    return escape(name).replace(/\+/g, '%2B');
}

function convertToUTF8(text) {
    var utf8Text = text;
    try {
        // hold the value when it's not utf8 text
        utf8Text = decodeURIComponent(escape(text));
    }catch(e) {
        // decode the value when it is utf8 text
        utf8Text = decodeNameWithHash(text);
    }
    return utf8Text;
}

function encodeToUTF8(text) {
    var utf8Text = text;
    try {
        // hold the value when it's not utf8 text
        utf8Text = encodeURIComponent(unescape(text));
    }catch(e) {
        // decode the value when it is utf8 text
        utf8Text = encodeNameWithHash(text);
    }
    return utf8Text;
}

function assembleHash (hash, params) {
    let result = {}
    if (hash) {
        let hashWithoutSharp = hash.substring(1);
        let listHashElement = hashWithoutSharp.split("&");
        let hashObject = {};
        listHashElement.map(e => {
            let abc = e.split('=');
            let key = abc[0];
            let value = abc[1];
            hashObject[key] = value
        })
        if (Array.isArray(params)) {
            for (let param of params) {
                result[param] = hashObject[param];
            }
        } else {
            result[params] = hashObject[params];
        }
    }
    return result;
}