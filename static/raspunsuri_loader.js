
self.onmessage = function genereaza_lista(e) {
    var ls_rasp = {}
    var i = 0
    const ls = e.data[0];
    const tot = e.data[1]

    let lasts = 0
  
    i = 0
    for(cuv of ls){
        for(cuv1 of tot){
            let raspuns = [0, 0, 0, 0, 0]
            let corect = cuv1
            for (let i = 0; i < 5; i++) {
                if(cuv[i] === corect[i]){
                raspuns[i] = 2
                corect = corect.replace(new RegExp(cuv[i], ''), '_');
                }
            }
            for (let i = 0; i < 5; i++) {
                if(raspuns[i] == 0 && corect.includes(cuv[i])){
                raspuns[i] = 1
                corect = corect.replace(new RegExp(cuv[i], ''), '_');
                }
            }
            rasp = raspuns.join("")
            if (!ls_rasp.hasOwnProperty(cuv)) {
                ls_rasp[cuv] = {};
            }
            if (!ls_rasp[cuv].hasOwnProperty(rasp)) {
                ls_rasp[cuv][rasp] = [];
            }

            ls_rasp[cuv][rasp].push(cuv1)
        }
        
        i += 1
      
        if(i % 100 === 0){
            
            postMessage([0,i-lasts])
            lasts = i
        }
    }

  
    postMessage([1,ls_rasp])
  };