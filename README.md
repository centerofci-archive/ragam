# Rāgam: 
Convert text (sāhitya) written in [Saṃskṛtam's](https://en.wikipedia.org/wiki/Sanskrit "Saṃskṛtam") [IAST](http://https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration "IAST") version to LaTeX

### Usage
Place your .txt IAST files in the raw_iast. Run the script. The output .tex files will be placed in iast_latex.
 

       .
        ├── iast_latex
        │   └── dharmaSamvardhani.tex
        ├── main.py
        ├── raw_iast
        │   └── dharmaSamvardhani.txt
        └── utils
            └── mapping.py    

`$ cat raw_iast/dharmaSamvardhani.txt`

    Pallavi 
    dharma  saṁvardhani danuja saṁardini  
    dharā dhara-ātmajē ajē dayayā māṁ pāhi pāhi
    
    Anupallavi  
    nirmala hr̥daya nivāsini nitya-ānanda vilāsini  
    karma jñānavidhāyini kāṅkṣita-artha pradāyini
    
    Caraṇam  
    mādhava sōdari sundari madhyamāvati śaṅkari  
    mādhurya vāg-vijr̥mbhiṇi mahā dēva kuṭumbini  
    sādhu jana citta ran̄jani śāśvata guru guha janani 
    bōdha rūpiṇi niran̄jani bhuvana-īśa durita bhan̄jani 
    pādaja viśva vilāsini pan̄ca nadī-īśa-ullāsini 
    vēda śāstra viśvāsini vidhi hari hara prakāśini

  ```$ python main.py
   Saving latex version of dharmaSamvardhani```

`$ cat iast_latex/dharmaSamvardhani.tex`

    Pallavi  
    dharma sa\.{m}vardhani danuja sa\.{m}ardini 
    dhar\=a dhara-\=atmaj\={e} aj\={e} dayay\=a m\=a\.{m} p\=ahi p\=ahi
    
    Anupallavi  
    nirmala hr̥daya niv\=asini nitya-\=ananda vil\=asini  
    karma j\~{n}\=ana vidh\=ayini k\=aṅk\d{s}ita-artha prad\=ayini
    
    Cara\d{n}am  
    m\=adhava s\={o}dari sundari madhyam\=avati \'{s}aṅkari 
    m\=adhurya v\=ag-vijr̥mbhi\d{n}i mah\=a d\={e}va ku\.{t}umbini 
    s\=adhu jana citta ran̄jani \'{s}\=a\'{s}vata guru guha janani 
    b\={o}dha r\={u}pi\d{n}i niran̄jani bhuvana-\={i}\'{s}a durita bhan̄jani 
    p\=adaja vi\'{s}va vil\=asini pan̄ca nad\={i}-\={i}\'{s}a-ull\=asini 
    v\={e}da \'{s}\=astra vi\'{s}v\=asini vidhi hari hara prak\=a\'{s}ini
