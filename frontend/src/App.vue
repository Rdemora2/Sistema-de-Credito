<template>
  <div>
    <form @submit.prevent="submitForm">
      <label for="nomeCompleto">Nome Completo:</label>
      <input
        v-model="formData.full_name"
        id="nomeCompleto"
        type="text"
        required
      />

      <label for="cpf">CPF:</label>
      <input v-model="formData.cpf" id="cpf" type="text" required />

      <label for="endereco">Endereço:</label>
      <input v-model="formData.address" id="endereco" type="text" required />

      <label for="valorEmprestimo">Valor do Empréstimo:</label>
      <input
        v-model="formData.loan_amount"
        id="valorEmprestimo"
        type="number"
        required
      />

      <button type="submit">Enviar</button>
    </form>
  </div>
  <div>
    <!-- Exibir o valor de credit_api_response -->
    <p>Resultado da API: {{ creditApiResponse }}</p>
  </div>
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
      creditApiResponse: null, // Inicialmente, o valor é nulo
    };
  },
  methods: {
    async submitForm() {
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

        await new Promise((resolve) => setTimeout(resolve, 23000));

        const creditApiResponse = await fetch(
          `http://localhost:8000/api/credit-forms/${id}/`
        );
        const creditApiData = await creditApiResponse.json();

        this.creditApiResponse = creditApiData.credit_api_response;
      } catch (error) {
        console.error("Erro ao enviar formulário:", error);
      }
    },
  },
};
</script>
