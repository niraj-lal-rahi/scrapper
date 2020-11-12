<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateEcourtDistrictsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('ecourt_districts', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->unsignedBigInteger('ecourt_states_id');
            $table->timestamps();

            $table->foreign('ecourt_states_id')->references('id')->on('ecourt_states');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('ecourt_districts');
    }
}
