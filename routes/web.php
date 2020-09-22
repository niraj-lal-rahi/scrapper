<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('home','IndexController@index');
Route::post('home','IndexController@create');

Route::get('delhi-high-court','DelhiHighCourtController@index');
Route::post('delhi-high-court','DelhiHighCourtController@store');

Route::get('jsearch','DelhiHighCourtController@jSearch');
Route::post('jsearch','DelhiHighCourtController@jSearchStore');
