<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class DelhiHighCourtController extends Controller
{
    //

    public function index(){
        $courts = array(
            // 'services-ecourts-gov-in.py' => 'https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/s_orderdate.php?state=D&state_cd=26&dist_cd=8',
            // 'main-sci-gov-in-daily-order.py' => 'https://main.sci.gov.in/daily-order',
            'delhihighcourt-nic-in-case.py' => 'http://delhihighcourt.nic.in/case.asp',
            // '164-100-69-66-jsearch.py' => 'http://164.100.69.66/jsearch/',
            // 'main-sci-gov-in-judgments.py' => 'https://main.sci.gov.in/judgments'

        );
        return view('Home.delhi',compact('courts'));
    }

    public function store(Request $request){
        try{

            $validate  = validator($request->all(),[
                'case_type' => 'required',
                'cyear' => 'required',
            ],[
                'case_type.required' => 'Select case type is required',
                'cyear.required' => 'Select year'
            ]);
            if($validate->fails()){
                return redirect()->back()->withErrors($validate->errors()->first());
            }
            $create = \App\DelhiHighCourtCase::create(
                [
                    "user_id" => 1,
                    "case_type" => $request->case_type,
                    "year" => $request->cyear,

                ]
            );
            $fileName = $request->court ??'delhihighcourt-nic-in-case.py';

            $process = new Process(['python3', base_path('python/'.$fileName),'-id',$create->id]);
            $process->run();

            if (!$process->isSuccessful()) {
                throw new ProcessFailedException($process);
            }

            echo $process->getOutput();


        }catch(\Exception $exception){
            return redirect()->back()->withErrors($exception->getMessage());
        }
    }

    public function jSearch(){
        $courts = array(
            // 'services-ecourts-gov-in.py' => 'https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/s_orderdate.php?state=D&state_cd=26&dist_cd=8',
            // 'main-sci-gov-in-daily-order.py' => 'https://main.sci.gov.in/daily-order',
            // 'delhihighcourt-nic-in-case.py' => 'http://delhihighcourt.nic.in/case.asp',
            '164-100-69-66-jsearch.py' => 'http://164.100.69.66/jsearch/',
            // 'main-sci-gov-in-judgments.py' => 'https://main.sci.gov.in/judgments'

        );
        return view('Home.jsearch',compact('courts'));
    }

    public function jSearchStore(Request $request){
        try{
            $validate  = validator($request->all(),[
                'fdate' => 'required',
            ],[
                'fdate.required' => 'Select date',
            ]);
            if($validate->fails()){
                return redirect()->back()->withErrors($validate->errors()->first());
            }

            $create = \App\JSearch::create([
                "date" => $request->fdate,

                "user_id" => 1
            ]);
            $fileName = $request->court;
            $process = new Process(['python3', base_path('python/'.$fileName),'-id',$create->id]);
            $process->run();

            if (!$process->isSuccessful()) {
                throw new ProcessFailedException($process);
            }

            echo $process->getOutput();
        }catch(\Exception $exception){
            return redirect()->back()->withErrors($exception->getMessage());
        }
    }
}
