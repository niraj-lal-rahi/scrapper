<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateDelhiHighCourtCasesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('delhi_high_court_cases', function (Blueprint $table) {
            $table->id();
            $table->integer('user_id')->default(0);
            $table->string('case_type');
            $table->string('no');
            $table->string("year");
            $table->longText('data')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('delhi_high_court_cases');
    }
}
