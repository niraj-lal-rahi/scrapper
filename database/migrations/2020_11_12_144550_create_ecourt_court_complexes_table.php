<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateEcourtCourtComplexesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('ecourt_court_complexes', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->text('value');
            $table->unsignedBigInteger('ecourt_districts_id');
            $table->timestamps();

            $table->foreign('ecourt_districts_id')->references('id')->on('ecourt_districts');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('ecourt_court_complexes');
    }
}
