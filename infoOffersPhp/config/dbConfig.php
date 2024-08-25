<?php

class Conexion {
    private $cdc = "pgsql:host=postgresql-progra.alwaysdata.net;port=5432;dbname=progra_offers;user=progra;password=123456Progra@";

    public function connect() {
        try {
            $conn = new PDO($this->cdc);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $a) {
            error_log("Error de conexión: " . $a->getMessage());
            return null;
        }
        return $conn;
    }
}

?>
