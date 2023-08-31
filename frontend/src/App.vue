<template>
  <div class="container">
    <form @submit.prevent="submitForm" class="form">
      <label for="nomeCompleto">Nome Completo:</label>
      <input
        v-model="formData.full_name"
        id="nomeCompleto"
        type="text"
        required
        class="input-field"
      />

      <label for="cpf">CPF:</label>
      <input
        v-model="formData.cpf"
        id="cpf"
        type="text"
        required
        class="input-field"
      />

      <label for="endereco">Endereço:</label>
      <input
        v-model="formData.address"
        id="endereco"
        type="text"
        required
        class="input-field"
      />

      <label for="valorEmprestimo">Valor do Empréstimo:</label>
      <input
        v-model="formData.loan_amount"
        id="valorEmprestimo"
        type="number"
        required
        class="input-field"
      />

      <button type="submit" class="submit-button">Enviar</button>
    </form>

    <div v-if="loading" class="loading-overlay">
      <div class="loading-spinner"></div>
      <p>Analisando sua proposta...</p>
    </div>

    <p v-if="creditApiResponse !== null" class="result">
      <span v-if="creditApiResponse === true" class="approved-message">
        Empréstimo pré-aprovado, encaminhado para análise mais aprofundada.
      </span>
      <span v-else-if="creditApiResponse === false" class="rejected-message">
        Que pena! No momento, não temos nenhum empréstimo disponível. Tente
        novamente em 90 dias.
      </span>
    </p>
  </div>
  <!-- Footer -->
  <footer class="footer">
    <div class="footer-content">
      <p>2023 - Roberto Moraes</p>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        nomeCompleto: "",
        cpf: "",
        endereco: "",
        valorEmprestimo: 0,
      },
      creditApiResponse: null,
      loading: false,
    };
  },
  methods: {
    async submitForm() {
      this.loading = true;

      try {
        const response = await fetch("http://localhost:8000/api/sis_credito/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.formData),
        });

        const data = await response.json();
        const id = data.id;

        await fetch(`http://localhost:8000/api/sis_credito/${id}/call_task/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            nomeCompleto: this.formData.nomeCompleto,
            cpf: this.formData.cpf,
          }),
        });

        await new Promise((resolve) => setTimeout(resolve, 25000));

        const creditApiResponse = await fetch(
          `http://localhost:8000/api/credit-forms/${id}/`
        );
        const creditApiData = await creditApiResponse.json();

        this.creditApiResponse = creditApiData.credit_api_response;
      } catch (error) {
        console.error("Erro ao enviar formulário:", error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 98vh;
  font-family: Arial, sans-serif;
}

.form {
  display: flex;
  flex-direction: column;
  width: 300px;
  margin-bottom: 20px;
}

.input-field {
  margin-bottom: 10px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.submit-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.loading-spinner {
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top: 4px solid #ffffff;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.result {
  margin-top: 20px;
  font-weight: bold;
}

/* Estilos para o Footer */
.footer {
  background-color: #333;
  color: white;
  padding: 20px 0;
  text-align: center;
  position: absolute;
  bottom: 0;
  width: 99%;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
}
</style>
