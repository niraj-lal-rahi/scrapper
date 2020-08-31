<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Base extends Model
{
    //
    protected $table = 'base';
    protected $fillable = ['frm_date','to_date','link','data'];
}
