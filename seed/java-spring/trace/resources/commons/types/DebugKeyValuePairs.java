/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.commons.types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(
    builder = DebugKeyValuePairs.Builder.class
)
public final class DebugKeyValuePairs {
  private final DebugVariableValue key;

  private final DebugVariableValue value;

  private DebugKeyValuePairs(DebugVariableValue key, DebugVariableValue value) {
    this.key = key;
    this.value = value;
  }

  @JsonProperty("key")
  public DebugVariableValue getKey() {
    return key;
  }

  @JsonProperty("value")
  public DebugVariableValue getValue() {
    return value;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof DebugKeyValuePairs && equalTo((DebugKeyValuePairs) other);
  }

  private boolean equalTo(DebugKeyValuePairs other) {
    return key.equals(other.key) && value.equals(other.value);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.key, this.value);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static KeyStage builder() {
    return new Builder();
  }

  public interface KeyStage {
    ValueStage key(DebugVariableValue key);

    Builder from(DebugKeyValuePairs other);
  }

  public interface ValueStage {
    _FinalStage value(DebugVariableValue value);
  }

  public interface _FinalStage {
    DebugKeyValuePairs build();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements KeyStage, ValueStage, _FinalStage {
    private DebugVariableValue key;

    private DebugVariableValue value;

    private Builder() {
    }

    @java.lang.Override
    public Builder from(DebugKeyValuePairs other) {
      key(other.getKey());
      value(other.getValue());
      return this;
    }

    @java.lang.Override
    @JsonSetter("key")
    public ValueStage key(DebugVariableValue key) {
      this.key = key;
      return this;
    }

    @java.lang.Override
    @JsonSetter("value")
    public _FinalStage value(DebugVariableValue value) {
      this.value = value;
      return this;
    }

    @java.lang.Override
    public DebugKeyValuePairs build() {
      return new DebugKeyValuePairs(key, value);
    }
  }
}