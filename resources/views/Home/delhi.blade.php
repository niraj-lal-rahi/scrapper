<!DOCTYPE html>
<html lang="en">
<head>
  <title>Home</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
    $( function() {
      $( "#fdate" ).datepicker({
        dateFormat: 'dd-mm-yy',
        maxDate: new Date()
      });
    } );
    $( function() {
      $( "#tdate" ).datepicker({
        dateFormat: 'dd-mm-yy',
        maxDate: new Date()
      });
    } );
    </script>
</head>
<body>

<div class="container">
  <h2>Court Data listing</h2>
  {{-- <div class="alert alert-success" role="alert">
    This is a success alert—check it out!
  </div> --}}
  @if(session('errors'))
  <div class="alert alert-danger" role="alert">
    {{session('errors')}}
  </div>
  @endif
  <form action="" method="POST">
      {{ csrf_field()}}
        <div class="form-group">
            <label for="email">Select Court:</label>
            <select id="courts" name="court" class="form-control" >
               @foreach ($courts as $key => $court)
                    <option value="{{$key}}">{{$court}}</option>
               @endforeach
            </select>
        </div>

        {{-- <div class="form-group">
            <input type="radio" id="order" name="type" value="order">
            <label for="order">Order</label><br>
            <input type="radio" id="judgments" name="type" value="judgments">
            <label for="judgments">Judgements</label><br>
        </div> --}}
    <div class="form-group">
        <label for="case-type">Case Type:</label>
        <select name="case_type" size="1" class="form-group" >
            <option value="ALL">ALL</option>

            <option value="ARB. A. (COMM.)">ARB. A. (COMM.) - [ARB]</option>

            <option value="ARB.A.">ARB.A. - [AAP]</option>

            <option value="ARB.P.">ARB.P. - [AA]</option>

            <option value="AW">AW - [AW]</option>

            <option value="BAIL APPLN.">BAIL APPLN. - [BAILA]</option>

            <option value="C.O.">C.O. - [XOBJ]</option>

            <option value="C.O.">C.O. - [CO]</option>

            <option value="C.R.P.">C.R.P. - [CR]</option>

            <option value="C.REF.(O)">C.REF.(O) - [CRO]</option>

            <option value="C.RULE">C.RULE - [CRULE]</option>

            <option value="CA">CA - [CAV]</option>

            <option value="CA">CA - [CAA]</option>

            <option value="CA">CA - [CAA]</option>

            <option value="CAVEAT(CO.)">CAVEAT(CO.) - [CAVE]</option>

            <option value="CC">CC - [CC]</option>

            <option value="CC(ARB.)">CC(ARB.) - [CCR]</option>

            <option value="CCP(CO.)">CCP(CO.) - [CCPCO]</option>

            <option value="CCP(O)">CCP(O) - [CCPO]</option>

            <option value="CCP(REF)">CCP(REF) - [CCPRF]</option>

            <option value="CEAC">CEAC - [CEAC]</option>

            <option value="CEAR">CEAR - [CEAR]</option>

            <option value="CF">CF - [CF]</option>

            <option value="CHAT.A.C.">CHAT.A.C. - [CHAC]</option>

            <option value="CHAT.A.REF">CHAT.A.REF - [CHAR]</option>

            <option value="CM APPL.">CM APPL. - [CM2]</option>

            <option value="CM APPL.">CM APPL. - [CM1]</option>

            <option value="CM(M)">CM(M) - [CMM]</option>

            <option value="CMI">CMI - [CMI]</option>

            <option value="CMI">CMI - [CMI]</option>

            <option value="CO.A(SB)">CO.A(SB) - [COASB]</option>

            <option value="CO.A(SB)">CO.A(SB) - [CO.A]</option>

            <option value="CO.APP.">CO.APP. - [COA]</option>

            <option value="CO.APPL.">CO.APPL. - [CA]</option>

            <option value="CO.APPL.(C)">CO.APPL.(C) - [CA(C)]</option>

            <option value="CO.APPL.(M)">CO.APPL.(M) - [CA(M)]</option>

            <option value="CO.EX.">CO.EX. - [CO.EX]</option>

            <option value="CO.PET.">CO.PET. - [CP]</option>

            <option value="CONT.APP.(C)">CONT.APP.(C) - [CCA]</option>

            <option value="CONT.CAS(C)">CONT.CAS(C) - [CCP]</option>

            <option value="CONT.CAS.(CRL)">CONT.CAS.(CRL) - [CRLCP]</option>

            <option value="CRL.A.">CRL.A. - [CRLA]</option>

            <option value="CRL.C.REF.">CRL.C.REF. - [CRLCR]</option>

            <option value="CRL.L.P.">CRL.L.P. - [CRLMP]</option>

            <option value="CRL.L.P.">CRL.L.P. - [CRLMA]</option>

            <option value="CRL.M.(BAIL)">CRL.M.(BAIL) - [CRLMB]</option>

            <option value="CRL.M.(CO.)">CRL.M.(CO.) - [CRLMC]</option>

            <option value="CRL.M.A.">CRL.M.A. - [CRLM]</option>

            <option value="CRL.M.C.">CRL.M.C. - [CRLMM]</option>

            <option value="CRL.M.I.">CRL.M.I. - [CRLMI]</option>

            <option value="CRL.O.">CRL.O. - [CRLO]</option>

            <option value="CRL.O.(CO.)">CRL.O.(CO.) - [CRLOC]</option>

            <option value="CRL.REF.">CRL.REF. - [CRLRF]</option>

            <option value="CRL.REV.P.">CRL.REV.P. - [CRLR]</option>

            <option value="CS(COMM)">CS(COMM) - [SC]</option>

            <option value="CS(OS)">CS(OS) - [S]</option>

            <option value="CS(OS) GP">CS(OS) GP - [SG]</option>

            <option value="CUS.A.C.">CUS.A.C. - [CUSAC]</option>

            <option value="CUS.A.R.">CUS.A.R. - [CUSAR]</option>

            <option value="CUSAA">CUSAA - [CUSAA]</option>

            <option value="CUSTOM A.">CUSTOM A. - [CUSA]</option>

            <option value="DEATH SENTENCE REF.">DEATH SENTENCE REF. - [MREF]</option>

            <option value="DEATH SENTENCE REF.">DEATH SENTENCE REF. - [DSRF]</option>

            <option value="EDA">EDA - [EDA]</option>

            <option value="EDC">EDC - [EDC]</option>

            <option value="EDR">EDR - [EDR]</option>

            <option value="EFA(OS)">EFA(OS) - [EFAOS]</option>

            <option value="EL.PET.">EL.PET. - [EP]</option>

            <option value="ETR">ETR - [ETR]</option>

            <option value="EX.APPL.(OS)">EX.APPL.(OS) - [EA]</option>

            <option value="EX.F.A.">EX.F.A. - [EFA]</option>

            <option value="EX.P.">EX.P. - [EX]</option>

            <option value="EX.S.A.">EX.S.A. - [ESA]</option>

            <option value="FAO">FAO - [FAO]</option>

            <option value="FAO(OS)">FAO(OS) - [FAOOS]</option>

            <option value="FAO(OS) (COMM)">FAO(OS) (COMM) - [FAC]</option>

            <option value="GCAC">GCAC - [GCAC]</option>

            <option value="GCAR">GCAR - [GCAR]</option>

            <option value="GTA">GTA - [GTA]</option>

            <option value="GTC">GTC - [GTC]</option>

            <option value="GTR">GTR - [GTR]</option>

            <option value="I.A.">I.A. - [IA]</option>

            <option value="I.P.A.">I.P.A. - [IPA]</option>

            <option value="ITA">ITA - [ITA]</option>

            <option value="ITC">ITC - [ITC]</option>

            <option value="ITR">ITR - [ITR]</option>

            <option value="ITSA">ITSA - [ITSA]</option>

            <option value="LA.APP.">LA.APP. - [LAA]</option>

            <option value="LPA">LPA - [LPA]</option>

            <option value="MAC.APP.">MAC.APP. - [MACA]</option>

            <option value="MAT.">MAT. - [MAT]</option>

            <option value="MAT.APP.">MAT.APP. - [MATA]</option>

            <option value="MAT.APP.(F.C.)">MAT.APP.(F.C.) - [MATFC]</option>

            <option value="MAT.CASE">MAT.CASE - [MATC]</option>

            <option value="MAT.REF.">MAT.REF. - [MATR]</option>

            <option value="NA">NA - [NA]</option>

            <option value="O.A.">O.A. - [OAA]</option>

            <option value="O.A.">O.A. - [OA]</option>

            <option value="O.M.P.">O.M.P. - [OMP]</option>

            <option value="O.M.P. (COMM)">O.M.P. (COMM) - [OMC]</option>

            <option value="O.M.P. (E) (COMM.)">O.M.P. (E) (COMM.) - [OME]</option>

            <option value="O.M.P. (J) (COMM.)">O.M.P. (J) (COMM.) - [OMJ]</option>

            <option value="O.M.P. (MISC.)">O.M.P. (MISC.) - [OMM]</option>

            <option value="O.M.P. (T) (COMM.)">O.M.P. (T) (COMM.) - [OMT]</option>

            <option value="O.M.P.(E)">O.M.P.(E) - [OE]</option>

            <option value="O.M.P.(EFA)(COMM.)">O.M.P.(EFA)(COMM.) - [OMA]</option>

            <option value="O.M.P.(I)">O.M.P.(I) - [OI]</option>

            <option value="O.M.P.(I) (COMM.)">O.M.P.(I) (COMM.) - [OMI]</option>

            <option value="O.M.P.(MISC.)(COMM.)">O.M.P.(MISC.)(COMM.) - [OMMC]</option>

            <option value="O.M.P.(T)">O.M.P.(T) - [OMPT]</option>

            <option value="O.REF.">O.REF. - [OREF]</option>

            <option value="O.REF.">O.REF. - [CRF]</option>

            <option value="OBJ. IN SUIT">OBJ. IN SUIT - [OBJ]</option>

            <option value="OCJA">OCJA - [OCJA]</option>

            <option value="OD">OD - [OD]</option>

            <option value="OLR">OLR - [OLR]</option>

            <option value="OMP (ENF.) (COMM.)">OMP (ENF.) (COMM.) - [OMF]</option>

            <option value="R.A.">R.A. - [RA]</option>

            <option value="RC.REV.">RC.REV. - [RCR]</option>

            <option value="RC.S.A.">RC.S.A. - [SAO]</option>

            <option value="RC.S.A.">RC.S.A. - [RCSA]</option>

            <option value="REVIEW PET.">REVIEW PET. - [RP]</option>

            <option value="RFA">RFA - [RFA]</option>

            <option value="RFA(OS)">RFA(OS) - [RFAOS]</option>

            <option value="RFA(OS)(COMM)">RFA(OS)(COMM) - [RFC]</option>

            <option value="RSA">RSA - [RSA]</option>

            <option value="SCA">SCA - [SCA]</option>

            <option value="SDR">SDR - [SDR]</option>

            <option value="SERTA">SERTA - [SERTA]</option>

            <option value="ST.APPL.">ST.APPL. - [STA]</option>

            <option value="ST.APPL.">ST.APPL. - [STC]</option>

            <option value="ST.REF.">ST.REF. - [STR]</option>

            <option value="STC">STC - [STC]</option>

            <option value="SUR.T.REF.">SUR.T.REF. - [SRTR]</option>

            <option value="TEST.CAS.">TEST.CAS. - [PR]</option>

            <option value="TR.P.(C)">TR.P.(C) - [TRP]</option>

            <option value="TR.P.(C.)">TR.P.(C.) - [TPC]</option>

            <option value="TR.P.(CRL.)">TR.P.(CRL.) - [TPCRL]</option>

            <option value="VAT APPEAL">VAT APPEAL - [VATA]</option>

            <option value="W.P.(C)">W.P.(C) - [CW]</option>

            <option value="W.P.(CRL)">W.P.(CRL) - [CRLW]</option>

            <option value="WTA">WTA - [WTA]</option>

            <option value="WTC">WTC - [WTC]</option>

            <option value="WTR">WTR - [WTR]</option>

        </select>
    </div>
    <div class="form-group">
      <label for="pwd">No:</label>
      <input name="cno" type="text" class="form-group" size="8">
    </div>

    <div class="form-group">
        <label for="pwd">Year:</label>
        <select name="cyear" id="c_year" class="form-group" >
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
            <option value="2017">2017</option>
            <option value="2016">2016</option>
            <option value="2015">2015</option>
            <option value="2014">2014</option>
            <option value="2013">2013</option>
            <option value="2012">2012</option>
            <option value="2011">2011</option>
            <option value="2010">2010</option>
            <option value="2009">2009</option>
            <option value="2008">2008</option>
            <option value="2007">2007</option>
            <option value="2006">2006</option>
            <option value="2005">2005</option>
            <option value="2004">2004</option>
            <option value="2003">2003</option>
            <option value="2002">2002</option>
            <option value="2001">2001</option>
            <option value="2000">2000</option>
            <option value="1999">1999</option>
            <option value="1998">1998</option>
            <option value="1997">1997</option>
            <option value="1996">1996</option>
            <option value="1995">1995</option>
            <option value="1994">1994</option>
            <option value="1993">1993</option>
            <option value="1992">1992</option>
            <option value="1991">1991</option>
            <option value="1990">1990</option>
            <option value="1989">1989</option>
            <option value="1988">1988</option>
            <option value="1987">1987</option>
            <option value="1986">1986</option>
            <option value="1985">1985</option>
            <option value="1984">1984</option>
            <option value="1983">1983</option>
            <option value="1982">1982</option>
            <option value="1981">1981</option>
            <option value="1980">1980</option>
            <option value="1979">1979</option>
            <option value="1978">1978</option>
            <option value="1977">1977</option>
            <option value="1976">1976</option>
            <option value="1975">1975</option>
            <option value="1974">1974</option>
            <option value="1973">1973</option>
            <option value="1972">1972</option>
            <option value="1971">1971</option>
            <option value="1970">1970</option>
            <option value="1969">1969</option>
            <option value="1968">1968</option>
            <option value="1967">1967</option>
            <option value="1966">1966</option>
            <option value="1965">1965</option>
            <option value="1964">1964</option>
            <option value="1963">1963</option>
            <option value="1962">1962</option>
            <option value="1961">1961</option>
            <option value="1960">1960</option>
            <option value="1959">1959</option>
            <option value="1958">1958</option>
            <option value="1957">1957</option>
            <option value="1956">1956</option>
            <option value="1955">1955</option>
            <option value="1954">1954</option>
            <option value="1953">1953</option>
            <option value="1952">1952</option>
            <option value="1951">1951</option>
            <option value="1950">1950</option>
            <option value="0">All Years</option>
        </select>
    </div>

    <button type="submit" class="btn btn-default">Submit</button>
  </form>
</div>

</body>
</html>
